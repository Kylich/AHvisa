# -*- coding: utf-8 -*-.
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
f = open('mct.txt', 'r', encoding='utf-8')

# photo=[
# """P<RUSCHUKINA<X<ELENA<<<<<<<<<<<<<<6£666KKKKKK
# 7224947463RUS8407177F2212245<<<<<<<<<<<<<<06""",

# """P<RUSURAEV<<ANDREY<<<<<<<<<<<<<esdsssssee<<<
# 7234631288RUS6407276M2303093<<<<<<<<<<<<<<02""",

# """P<RUSASTANIN<<SERGEY<<<<<<<<<<<<<<KKKKKKKKK
# 7152939691RUS6405216M2107110<<<<<<<<<<<<<<08""",

# """P<RUSDUBOVITSKAYA<<NATALIA<<<<<<<KKKKEKE
# 5156003039RUS7312151F1710102<<<<cccceces<x<d""",

# """P<RUSGRAN<<SERGEI<<<<<<<<<<<K<<Ke<<esss<<<<<<
# 7179677969RUS8607151M2203023<<<<<<<<<<<<<<00"""]
passAll = []

def KSch(KS, KS_):
    KSves = ([7, 3, 1] * 3)
    KSmap = []
    for i in range(0,len(KS_)):
        KSmap.append(int(list(KS_)[i])*KSves[i])
    KSch = sum(KSmap) % 10
    if KSch != int(KS):
        print('%s: wrong KS = %s' % ph, KS)
        return False
    return True

for ph in range(1,6):
    while True:
        imageMCT = Image.open('scan test\\00%sfull.jpg' % ph)
        textMCT = pytesseract.image_to_string(imageMCT, lang="eng")
        textMCT = textMCT.replace(' ', '')
        passData = {}
        MCTs = textMCT.split("\n")
        MCTwith=[]
        for s in MCTs:
            if '<' in s:
                MCTwith.append(s)
        
        if len(MCTwith)<2:
            print('%s: wrong len:\n\n\n%s' % (ph, textMCT))
            break      

        MCT1 = MCTwith[0]
        MCT2 = MCTwith[1]

        FNm = MCT1.find('<', 2)
        z=0
        while True:
            if MCT1[FNm+1] != '<':
                MCT1 = MCT1[:FNm+1] + MCT1[FNm+2:]
                if z>1:
                    print('%s: wrong FN' % ph)
                    break
                z+=1
            else: break
        
        FNe = MCT1.find('<', FNm+2)

        country = MCT1[2:5]
        surname = MCT1[5:FNm]
        name = MCT1[FNm+2:FNe]
        serial = MCT2[0:9]
        
        if not KSch(MCT2[9], serial): break

        Bcountry = MCT2[10:13]
        
        if not KSch(MCT2[19], MCT2[13:19]): break

        Byear = MCT2[13:15]
        Bmonth = MCT2[15:17]
        Bday = MCT2[17:19]

        sex = MCT2[20]

        passdate = MCT2[21:27]
        if not KSch(MCT2[27], passdate): break

        Pyear = MCT2[21:23]
        Pmonth = MCT2[23:25]
        Pday = MCT2[25:27]

        passData ['country'] = country
        passData ['surname'] = surname
        passData ['name'] = name
        passData ['serial'] = serial
        passData ['Bcountry'] = Bcountry
        passData ['Byear'] = Byear
        passData ['Bmonth'] = Bmonth
        passData ['Bday'] = Bday
        passData ['Pyear'] = Pyear
        passData ['Pmonth'] = Pmonth
        passData ['Pday'] = Pday
        
        passAll.append(passData)
        print('%s: good' % ph)
        break

# f.close