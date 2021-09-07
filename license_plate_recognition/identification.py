import cv2
import numpy as np
import io
import requests
import pytesseract
from PIL import Image

# image = "C:\\Users\\User\\Desktop\\hillarywebb\\eng_bw.png"

class IdentifyImage:

    def __init__(self, image_link):

        response = requests.get(image_link)
        # print( type(response) ) # <class 'requests.models.Response'>
        self.image = Image.open(io.BytesIO(response.content))
        # print( type(img) ) # <class 'PIL.JpegImagePlugin.JpegImageFile'>
        self.number = pytesseract.image_to_string(self.image)
    
    def getnumber(self):
        return self.number


# identifyImage(image).getnumber()