import cv2
import numpy as np
import pytesseract
from pytesseract import Output

image = "C:\\Users\\User\\Desktop\\hillarywebb\\eng_bw.png"

class identifyImage:

    def __init__(self, image_link):
        self.image = cv2.imread(image_link)
        self.number = pytesseract.image_to_string(self.image)
    
    def getnumber(self):
        return self.number


identifyImage(image).getnumber()