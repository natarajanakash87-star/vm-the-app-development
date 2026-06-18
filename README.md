# vm-the-app-development
# 🚀 Real-Time Object Detection and Tracking using YOLOv8

A Python-based real-time object detection and tracking application built with **Ultralytics YOLOv8** and **OpenCV**. The program can detect and track multiple objects from a webcam or a video file while displaying live FPS (Frames Per Second).

---

## 📌 Features

* 🎯 Real-time object detection using YOLOv8
* 🔄 Multi-object tracking with persistent IDs
* 📷 Supports webcam and video files
* ⚡ Live FPS counter
* 🖥️ Automatic webcam fallback if the default camera is unavailable
* ❌ Press **Q** to exit the application

---

## 🛠️ Technologies Used

* Python 3.x
* Ultralytics YOLOv8
* OpenCV
* argparse
* time

---

## 📂 Project Structure

```
project/
│── object_detection.py
│── requirements.txt
│── README.md
```

---

## 📥 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/yolo-object-tracking.git
cd yolo-object-tracking
```

### 2. Install dependencies

```bash
pip install ultralytics opencv-python
```

or

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Run using webcam

```bash
python object_detection.py
```

or

```bash
python object_detection.py --source 0
```

### Run using another webcam

```bash
python object_detection.py --source 1
```

### Run using a video file

```bash
python object_detection.py --source video.mp4
```

---

## ⚙️ How It Works

1. Loads the pretrained **YOLOv8 Nano (`yolov8n.pt`)** model.
2. Opens the selected webcam or video source.
3. Captures frames continuously.
4. Performs object detection and tracking.
5. Draws bounding boxes and tracking information.
6. Calculates and displays the current FPS.
7. Shows the processed video in real time.
8. Exits when the user presses **Q**.

---

## 📷 Sample Output

```
-----------------------------------------
| FPS: 32                               |
|                                       |
|   [Person]  ID:1                      |
|   ┌───────────────┐                   |
|   │               │                   |
|   │    PERSON     │                   |
|   │               │                   |
|   └───────────────┘                   |
|                                       |
-----------------------------------------
```

---

## 📋 Command Line Arguments

| Argument             | Description          |
| -------------------- | -------------------- |
| `--source 0`         | Use default webcam   |
| `--source 1`         | Use secondary webcam |
| `--source video.mp4` | Use a video file     |

---

## 📦 Dependencies

```
ultralytics
opencv-python
```

---

## 📈 Future Improvements

* Object counting
* Line crossing detection
* Speed estimation
* Face detection integration
* GPU optimization
* Save processed video output
* Email or alert notifications

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push to your fork
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Akash N**

* 🎓 B.E. Computer Science and Engineering (AI)
* Chennai Institute of Technology
* Passionate about AI, Computer Vision, and Full-Stack Development

⭐ If you found this project useful, don't forget to **star the repository**!
