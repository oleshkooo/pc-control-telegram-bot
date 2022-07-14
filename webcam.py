
import cv2
cam = cv2.VideoCapture(0)
result, image = cam.read()
if result:
	cv2.imwrite("GeeksForGeeks.png", image)
else:
	print("No image detected. Please! try again")
