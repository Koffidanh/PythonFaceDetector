import cv2
#Load some pre-trained data on face frontals from opencv 
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_alt_tree.xml')

# Choose an image to detect faces in
img = cv2.imread('img\download (5).jpg')
# Convert to grayscale
grayScaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
face_coordinates = trained_face_data.detectMultiScale(grayScaled_img)

# Draw rectangles around the faces
(x,y,w,h) = face_coordinates[0]
cv2.rectangle(img, (x, y),(x+w, y+h), (0,255,0), 2)

# print(face_coordinates)

#
cv2.imshow('ShowFace', img)
cv2.waitKey()



print("\nCode Completed\n")