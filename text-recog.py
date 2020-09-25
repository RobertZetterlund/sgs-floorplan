from cv2 import cv2
import pytesseract as pyt
import matplotlib.pyplot as plt

img = cv2.imread("beligium.png")

print(img)

text = pyt.image_to_string(img)

print(text)