# 📸 Face Filter using Computer Vision

## 📌 Project Overview

This project implements real-time Snapchat-style face filters using computer vision and facial landmark detection.

The application captures live video from a webcam, detects faces, identifies facial landmarks, and overlays virtual filters such as glasses, masks, hats, dog ears, or other augmented reality (AR) effects.

The project demonstrates the use of computer vision techniques for real-time image processing and augmented reality applications.

---

## ✨ Features

* Real-time webcam feed
* Face detection and tracking
* Facial landmark detection
* Multiple filter support
* Dynamic filter resizing and positioning
* Smooth overlay rendering
* Easy to add custom filters

---

## 🧠 How It Works

The application follows this workflow:

1. Capture video frames from the webcam
2. Detect faces in each frame
3. Identify facial landmarks
4. Calculate filter position and scale
5. Overlay the selected filter image
6. Display the processed frame in real time

---

## 🏗️ Project Structure

```text
snap-filter/
│
├── filters/
│   ├── glasses.png
│   ├── dog_ears.png
│   ├── hat.png
│   └── mask.png
│
├── assets/
│   └── sample_output.png
│
├── models/
│   └── face_landmark_model
│
├── main.py
├── utils.py
├── requirements.txt
└── README.md
```

---

## 🛠️ Technologies Used

* Python
* OpenCV
* MediaPipe
* NumPy

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/snap-filter.git
```

Move to the project directory:

```bash
cd snap-filter
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the application:

```bash
python main.py
```

Controls:

* Press `q` to exit the application
* Use keyboard shortcuts (if implemented) to switch filters

---

## 📷 Supported Filters

* Sunglasses
* Face masks
* Hats
* Dog ears
* Mustache
* Custom PNG overlays

> Filters should have transparent backgrounds (PNG format) for best results.

---

## 📈 Applications

* Social media filters
* Augmented reality experiences
* Virtual try-on systems
* Entertainment applications
* Computer vision learning projects

---

## 🔮 Future Improvements

* Multiple face support
* Gesture-based filter switching
* Hand tracking integration
* Emotion-based filter recommendations
* Mobile application deployment
* Save photos and videos
* Deploy as a web application

---

## 📸 Demo

Add screenshots or GIFs inside the `assets/` folder.

```markdown
![Demo](assets/sample_output.png)
```

---

## 🤝 Contributing

Contributions and suggestions are welcome.

Feel free to fork this repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Dev Patel**

SYBCA (AI) Student | Aspiring AI/ML Engineer
