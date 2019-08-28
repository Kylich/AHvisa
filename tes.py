#!/bin/env python
# -*- coding: utf-8 -*-.
 
import os
from PIL import Image
import pytesseract
import re

image = Image.open('001.jpg')
text = pytesseract.image_to_string(image, lang="rus")

print(text)