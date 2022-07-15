from cv2 import VideoCapture,imwrite
from os.path import abspath

camera = VideoCapture(0)
PATH = abspath('./')
for i in range(10):
    result, image = camera.read()
imwrite(PATH + '\Webcam.png', image)