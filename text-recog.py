from cv2 import cv2
import pytesseract as pyt
import matplotlib.pyplot as plt
import glob 

img = cv2.imread("downloads/file1450.png")

text = pyt.image_to_string(img)

print(text)