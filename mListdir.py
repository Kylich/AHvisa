import os
import datetime

import mTesseact

today = datetime.datetime.today().strftime("%Y-%m-%d")
pathToday = os.getcwd() + '\\temp\\%s\\' % today
path_to_watch = os.getcwd() + '\\temp\\%s\\scan\\' % today
before = dict ([(f, None) for f in os.listdir (path_to_watch)])

def l():
    global before
    after = dict ([(f, None) for f in os.listdir (path_to_watch)])
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]
    if added:
        print ("Added jpg: ", ", ".join (added))
        if len(added) == 1:
            mTesseact.ocr(added[0], path_to_watch)
        else:
            for ad in added:
                mTesseact.ocr(ad, path_to_watch)
    if removed: print ("Removed jpg: ", ", ".join (removed))
    before = after
