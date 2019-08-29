# -*- coding: utf-8 -*-.
 
#from PIL import Image
#import pytesseract
#import sys

#sys.path.append('C:\Program Files\Tesseract-OCR')
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#image = Image.open('003.jpg')
#MCT = pytesseract.image_to_string(image)
MCT = 'P<RUSAS TANIN<<SERGEY <<<<<<<<<<< <<< KKK KKK KKK\n7152939691RUS6405216M2107110<<<<<<<<<<<<<<08'
MCT = MCT.replace(' ', '')
MCTs = MCT.split("\n")

def serialKSch(serialKS, serial):
    serialKSves = [7, 3, 1] * 3
    serialKSmap = []
    for i in range(0,9):
        serialKSmap.append(int(list(serial)[i])*serialKSves[i])
    serialKScheck = sum(serialKSmap) % 10
    if serialKScheck != serialKS:
        print('wrong serialKS')
        input()

FNm = MCTs[0].find('<<')
FNe = MCTs[0].find('<<', FNm+2)

contry = MCTs[0][2:5]
family = MCTs[0][5:FNm]
name = MCTs[0][FNm+2:FNe]


serial = MCTs[1][0:9]

serialKSch(int(MCTs[1][9], serial)