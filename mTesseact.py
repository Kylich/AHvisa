from PIL import Image
import pytesseract
import mSQL
def ocr(ph, path_to_watch):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def KSch(KS, KS_):
        KSves = ([7, 3, 1] * 3)
        KSmap = []
        for i in range(0,len(KS_)):
            try:
                KSmap.append(int(list(KS_)[i])*KSves[i])
            except:
                print('%s: wrong KS numbers %s' % (ph, list(KS_)[i]))
                return False
        KSch = sum(KSmap) % 10
        if KSch != int(KS):
            print('%s: wrong KS = %s' % ph, KS)
            return False
        return True

    def FN(MCT1):
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
        return FNm, FNe

    while True:
        imageName = path_to_watch + ph
        imageMCT = Image.open(imageName)
        config_='--psm 3 --oem 1'
        textMCT = pytesseract.image_to_string(
            imageMCT,
            lang="eng",
            config=config_,
            )

        textMCT = textMCT.replace(' ', '')
        MCTs = textMCT.split("\n")
        passData = []
        MCTwith = []
        for s in MCTs:
            if '<' in s:
                MCTwith.append(s)
        
        if len(MCTwith)!=2:
            print('%s: wrong len - %s' % (ph, len(MCTwith)))
            print(MCTwith)
            break      

        MCT1 = MCTwith[0]
        MCT2 = MCTwith[1]

        FNm, FNe =  FN(MCT1)

        if not KSch(MCT2[9], MCT2[0:9]): break
        if not KSch(MCT2[19], MCT2[13:19]): break
        if not KSch(MCT2[27], MCT2[21:27]): break

        passData.append(MCT1[5:FNm])
        passData.append(MCT1[FNm+2:FNe])
        passData.append(MCT2[20])
        passData.append(MCT1[2:5])
        
        passData.append(MCT2[10:13])
        passData.append(MCT2[13:15])
        passData.append(MCT2[15:17])
        passData.append(MCT2[17:19])
        
        passData.append(MCT2[0:9])
        passData.append(MCT2[21:23])
        passData.append(MCT2[23:25])
        passData.append(MCT2[25:27])

        print('%s: good' % ph)
        mSQL.newClient(passData)
        break
    