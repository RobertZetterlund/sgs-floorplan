from cv2 import cv2
import pytesseract as pyt
import matplotlib.pyplot as plt
import glob 

img = cv2.imread("downloads/file1450.png")
# preprocess https://stackoverflow.com/a/60161328
# edges ? https://towardsdatascience.com/edge-detection-in-python-a3c263a13e03
# https://scikit-image.org/docs/dev/auto_examples/edges/plot_canny.html


text = pyt.image_to_string(img, lang="swe")

print(text)