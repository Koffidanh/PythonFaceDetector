# PythonFaceDetector

**PythonFaceDetector** is a simple face detection tool designed to detect frontal faces in images or videos using the **OpenCV** library. It allows users to run face detection on both static images and live webcam feeds.

## Features

- **Image Detection**: Detects faces in images and highlights them with rectangles.
- **Video Detection**: Detects faces in real-time using a webcam feed and displays the faces with rectangles.
- **OpenCV-Based**: Utilizes pre-trained models from OpenCV's `haarcascade_frontalface_alt_tree.xml` for detecting frontal faces.

## Prerequisites

- **Python 3.x**
- **OpenCV**: Install OpenCV using pip
    ```bash
    pip install opencv-python
    ```

## Getting Started

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/PythonFaceDetector.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd PythonFaceDetector
    ```

3. **Run the face detection script**:
    ```bash
    python face_detector.py
    ```

4. **Choose between image or video detection**:
    - Type `img` for detecting faces in an image.
    - Type `vid` for detecting faces in a video (webcam).

## How It Works

The face detector provides two modes of operation:

### Image Detection
If you choose **image** mode, the script will:
- Load a sample image (`img/download (5).jpg`).
- Convert the image to grayscale.
- Detect faces and draw rectangles around them.
- Display the image with the detected faces.

### Video Detection
If you choose **video** mode, the script will:
- Access your computer's webcam feed.
- Continuously detect faces in real-time.
- Draw rectangles around detected faces on each frame.
- Display the video feed with the detected faces.



else:
    print("\nCode Completed\n")
Resources
OpenCV Documentation: OpenCV.org
CleverProgrammer: Helpful tutorials on OpenCV and Python.
License
This project is licensed under the MIT License - see the LICENSE file for details.
