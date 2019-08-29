# -*- coding: utf-8 -*-.
from PIL import Image
import pytesseract
#import sys

#sys.path.append('C:\Program Files\Tesseract-OCR')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

for photo in range(1,6):
    imageMCT = Image.open('scan test\\00%smct.jpg' % photo)
    textMCT = pytesseract.image_to_string(imageMCT, lang="eng")
    textMCT = textMCT.replace(' ', '')
    
    MCTs = textMCT.split("\n")

    MCT1 = MCTs[0]
    MCT2 = MCTs[1]

    def KSch(KS, KS_):
        KSves = ([7, 3, 1] * 3)
        KSmap = []
        for i in range(0,len(KS_)):
            KSmap.append(int(list(KS_)[i])*KSves[i])
        KSch = sum(KSmap) % 10
        if KSch != int(KS):
            print(str(photo) + ' wrong KS ' + KS)
            input()

    FNm = MCT1.find('<')
    if MCT1[FNm+1] != '<':
        FNm = MCT1.find('<', FNm+1)
    FNe = MCT1.find('<', FNm+2)

    country = MCT1[2:5]
    sername = MCT1[5:FNm]
    name = MCT1[FNm+2:FNe]

    serial = MCT2[0:9]
    KSch(MCT2[9], serial)

    countryCh = MCT2[10:13]
    if countryCh != country:
        print(str(photo) + ' wrong country')
        input()

    KSch(MCT2[19], MCT2[13:19])

    Byear = MCT2[13:15]
    Bmonth = MCT2[15:17]
    Bday = MCT2[17:19]

    sex = MCT2[20]

    passdate = MCT2[21:27]
    KSch(MCT2[27], passdate)
