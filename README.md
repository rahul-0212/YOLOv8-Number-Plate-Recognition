# 🚗 AI Number Plate Recognition System

This project is an AI-based Vehicle Number Plate Recognition System built using Python.
It detects vehicle license plates in real-time using a webcam and extracts the plate number automatically.

The system uses a deep learning model for detection and OCR for reading the license plate text.

---

## 🔧 Technologies Used

* Python
* OpenCV
* YOLOv8
* EasyOCR

---

## ✨ Features

* Real-time number plate detection using webcam
* Automatic license plate number recognition
* Bounding box around detected plates
* Extracted number displayed on screen
* Works with live camera input

---

## 📂 Project Structure

```
number_plate_project
│
├── number_plate_yolo.py
├── number_plate.py
├── plate_model.pt
│
├── model
│   └── haarcascade_russian_plate_number.xml
│
├── plates
│   └── saved_images
│
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/your-username/YOLOv8-Number-Plate-Recognition.git
```

### 2. Go to the project folder

```
cd YOLOv8-Number-Plate-Recognition
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

or install manually:

```
pip install opencv-python
pip install ultralytics
pip install easyocr
```

### 4. Run the program

```
python number_plate_yolo.py
```

---

## 📸 Output

* Webcam opens
* Vehicle number plate is detected
* Plate number is extracted and displayed on the screen

---

## 🚀 Future Improvements

* Save detected plate numbers in a database
* Create a parking management system
* Improve detection accuracy using a custom trained model
* Add support for multiple cameras

---

## 👨‍💻 Author

Developed as a Computer Vision project using Python and AI technologies.
