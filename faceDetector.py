import cv2
# Load some pre-trained data on face frontals from opencv
trained_face_data = cv2.CascadeClassifier(
    'haarcascade_frontalface_alt_tree.xml')

# Choose an image to detect faces in
img = cv2.imread('img\images (7).jpg')

# To capture video from webcam
# webcam = cv2.VideoCapture(0)

# Iterate forever over frames
# while True:

# Read the current frame
# successful_frame_read, frame = webcam.read()
# Convert to grayscale
grayScaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
face_coordinates = trained_face_data.detectMultiScale(grayScaled_img)

# Draw rectangles around the faces
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(grayScaled_img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# print(face_coordinates)

# Display the image with the faces
cv2.imshow('ShowFace', grayScaled_img)
key = cv2.waitKey()

# Stop if Q key is pressed
# if key == 81 or key == 113:
# break

# Release the videoCapture object

# webcam.release()

print("\nCode Completed\n")
