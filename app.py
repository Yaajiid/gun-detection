from flask import Flask, render_template, Response, jsonify
import cv2
from ultralytics import YOLO
import time
from collections import deque, Counter
from playsound import playsound
import threading
import os
from datetime import datetime

app = Flask(__name__)

# Load YOLO model
yolo_model = YOLO("Guns_detection_model.pt")
cap = cv2.VideoCapture(0) # Membuka webcam secara realtime

# Thresholds
LOW_CONF = 0.3
HIGH_CONF = 0.6

# Voting buffer
DETECTION_BUFFER_SIZE = 5
detection_buffer = deque(maxlen=DETECTION_BUFFER_SIZE)

# Snapshot folder and status
SNAPSHOT_FOLDER = "snapshots"
os.makedirs(SNAPSHOT_FOLDER, exist_ok=True)
last_snapshot_filename = None
has_detected_gun = False

# Play alert sound
def play_alert():
    playsound("alert.mp3")

# Save snapshot image
def save_snapshot(frame, label):
    global last_snapshot_filename
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f"{timestamp}_{label}.jpg"
    filepath = os.path.join(SNAPSHOT_FOLDER, filename)
    cv2.imwrite(filepath, frame)
    last_snapshot_filename = filename
    print(f"[SNAPSHOT] {filename}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/snapshot/latest')
def latest_snapshot():
    global last_snapshot_filename
    if last_snapshot_filename:
        return jsonify({'snapshot': last_snapshot_filename})
    return jsonify({'snapshot': None})

@app.route('/video')
def video():
    def gen_frames():
        global has_detected_gun
        prev_time = time.time()

        while True:
            success, frame = cap.read()
            if not success:
                break

            results = yolo_model(frame)[0] # Mendeteksi apakah ada senjata dalam frame
            detected_labels = []

            for box in results.boxes:
                conf = float(box.conf[0])
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                if conf < LOW_CONF:
                    label = 'Not a Gun'
                    color = (0, 0, 255)
                elif conf < HIGH_CONF:
                    label = 'Possible a Gun'
                    color = (0, 255, 255)
                else:
                    cls = int(box.cls[0])
                    label = results.names[cls]
                    color = (0, 255, 0)

                detected_labels.append(label)
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2) # Memberikan anotasi (bounding box + confidence)
                cv2.putText(frame, f'{label} ({conf:.2f})', (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
                print(f'[DETECTED] {label} - Confidence: {conf:.2f}')

            if detected_labels:
                detection_buffer.append(tuple(detected_labels))

            all_labels = [label for group in detection_buffer for label in group]
            if all_labels:
                most_common_label, freq = Counter(all_labels).most_common(1)[0]
                cv2.putText(frame, f'Stabil: {most_common_label} ({freq}/{len(all_labels)})',
                            (10, frame.shape[0] - 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

                if most_common_label.lower() == 'gun':
                    if not has_detected_gun:
                        save_snapshot(frame, most_common_label) # Menyimpan snapshot saat senjata terdeteksi
                        threading.Thread(target=play_alert, daemon=True).start() # Memutar suara alarm (alert.mp3)
                        has_detected_gun = True
                else:
                    has_detected_gun = False

            # FPS Counter
            current_time = time.time()
            fps = 1 / (current_time - prev_time)
            prev_time = current_time
            cv2.putText(frame, f'FPS: {fps:.2f}', (10, 30), # Menampilkan FPS
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
