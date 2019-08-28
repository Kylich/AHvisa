# -*- coding: utf-8 -*-.
 
from PIL import Image
import pytesseract

image = Image.open('001.jpg')
text = pytesseract.image_to_string(image, lang="rus")

print(text)