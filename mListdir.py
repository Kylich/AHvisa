import os
import time

import mTesseact

path_to_watch = os.getcwd() + "\\scan"
before = dict ([(f, None) for f in os.listdir (path_to_watch)])
while 1:
    time.sleep (10)
    after = dict ([(f, None) for f in os.listdir (path_to_watch)])
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]
    if added:
        print ("Added: ", ", ".join (added))
        if len(added)==1:
            mTesseact.ocr(added[0])
        else:
            for ad in added:
                mTesseact.ocr(ad)
    if removed: print ("Removed: ", ", ".join (removed))
    before = after