# 🔫 Gun Detection System using YOLOv10

This project is an AI-powered firearm detection system that leverages **Computer Vision** and the **YOLOv10** deep learning model to automatically detect the presence of firearms in images or live video streams.

The system is designed to work quickly and accurately — even under challenging visual conditions such as low lighting or partially visible weapons.

---

## 🚀 Features

✅ Powered by YOLOv10, the system can:
- Detect firearms in real-time video feed  
- Trigger snapshot capture upon detection  
- Play an audible alert when a weapon is detected  
- Display the latest detection snapshot on the main interface  
- Allow users to manually upload an image for analysis  

---

## 🛠 Technologies Used

- Python  
- OpenCV  
- Flask (Web Interface)  
- YOLOv10 (via Ultralytics)  
- HTML / CSS / JavaScript (Frontend)  

---

## ⚙️ How It Works

1. The system captures live video using a webcam.  
2. YOLOv10 analyzes each frame to identify potential firearms.  
3. When a gun is detected:  
   - A snapshot of the frame is automatically saved  
   - An alert sound (`alert.mp3`) is played  
   - The snapshot is displayed on the main webpage  
4. Users can also upload images manually for one-time firearm detection  

---

## 📷 Interface Preview
Gun:

![Image](https://github.com/user-attachments/assets/4c9b1ee7-b736-47da-b766-818895a1be6d)

Not Gun:

![Image](https://github.com/user-attachments/assets/b2585e17-acd5-40a9-aede-cd45265a7d88)

---

## 🧭 Suitable For Use In

- 🛫 Airports, harbors, and national borders  
- 🏛 Government buildings  
- 🏫 Schools and universities  
- 🏢 Shopping malls and commercial centers  
- 🎤 Stadiums and concert venues  
- 🏛 Correctional facilities  
- 🏦 Banks and financial institutions  

---

## 📁 Project Folder Structure (Optional)

![Image](https://github.com/user-attachments/assets/723a8841-aa58-48c8-af80-2c1d96eb8453)

---

## 🛠 How To Run Project

```bash
# 1. Clone this repository
git clone https://github.com/username/gun-detection-system.git
cd gun-detection-system

# 2. Run the project
python app.py
