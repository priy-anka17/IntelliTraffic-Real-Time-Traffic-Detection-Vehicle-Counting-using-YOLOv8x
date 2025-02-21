# 🚦 IntelliTraffic: Real-Time Traffic Detection & Vehicle Counting using YOLOv8x

This project implements **real-time traffic detection and vehicle counting** using the **YOLOv8x** object detection model. It processes video streams to detect vehicles, classify them, and display live FPS performance.

## 📌 Features
- **🚗 Vehicle Detection & Counting**: Detects and counts cars, trucks, buses, and motorcycles.
- **📊 FPS Counter**: Monitors real-time processing speed.
- **🎯 Bounding Boxes & Labels**: Draws boxes around detected objects with confidence scores.
- **⚡ Optimized Processing**: Uses CUDA acceleration if available.

## 📂 Project Structure
```bash
├── traffic.mp4         # Sample traffic video
├── detect_traffic.py   # Main Python script
├── README.md           # Project Documentation
├── requirements.txt    # Dependencies
```

## 🛠 Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/traffic-detection.git
   cd traffic-detection
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download YOLOv8x model**
   ```bash
   wget https://github.com/ultralytics/assets/releases/download/v8/yolov8x.pt
   ```

## 🚀 Usage
Run the detection script:
```bash
python detect_traffic.py
```

To quit, press **'q'**.

## 🖥 Demo Output
![Traffic Detection](https://user-images.githubusercontent.com/example/demo.gif)

## 📝 To-Do
- [ ] Implement speed estimation
- [ ] Add vehicle tracking using SORT/DeepSORT
- [ ] Deploy as a web application

## 🤝 Contributing
Contributions are welcome! Feel free to fork this repository and submit pull requests.

## 📜 License
This project is licensed under the **MIT License**.
