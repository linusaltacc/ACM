import cv2
import pytesseract
from signtalon import *
# from signtalon import get_signature
def ocr(image):
    img = cv2.imread(image)
    out_below = pytesseract.image_to_string(img)
    return out_below
