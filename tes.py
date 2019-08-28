# -*- coding: utf-8 -*-.
 
from PIL import Image
import pytesseract
#import sys

#sys.path.append('C:\Program Files\Tesseract-OCR')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image = Image.open('001.jpg')
text = pytesseract.image_to_string(image, lang="rus")

print(text)