🔫 Gun Detection System using YOLOv10
This project is an AI-powered firearm detection system that leverages Computer Vision and the YOLOv10 deep learning model to automatically detect the presence of firearms in images or live video streams. The system is designed to work quickly and accurately, even under challenging visual conditions such as low lighting or partially visible weapons.
Powered by YOLOv10, the system can:
- Detect firearms in real-time video feeds
- Trigger snapshot capture upon detection
- Play an audible alert when a weapon is detected
- Display the latest detection snapshot on the main interface
- Allow users to manually upload an image for analysis

🛠 Technologies Used
- Python
- OpenCV
- Flask (Web Interface)
- YOLOv10 (via Ultralytics)
- HTML/CSS/JavaScript (Frontend)

⚙️ How It Works
1. The system captures live video using a webcam.
2. YOLOv10 analyzes each frame to identify potential firearms.
3. When a gun is detected:
   - A snapshot of the frame is automatically saved
   - An alert sound (alert.mp3) is played
   - The snapshot is displayed on the main webpage
4. Users can also upload images manually for one-time firearm detection

📷 Interface Preview

💡 Real-time detection with visual and audio feedback

