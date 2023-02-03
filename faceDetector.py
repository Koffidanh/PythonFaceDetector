import cv2
#Laoad some pre-trained data on face frontals from opencv 
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_alt_tree.xml')

# Choose an image to detect faces in
img = cv2.imread('img\download (5).jpg')

print("\nCode Completed\n")