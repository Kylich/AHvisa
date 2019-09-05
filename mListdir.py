import os
import mTesseact

def l(before, path_to_watch):
    after = dict ([(f, None) for f in os.listdir (path_to_watch)])
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]
    if added:
        print ("Added jpg: ", ", ".join (added))
        if len(added) == 1:
            mTesseact.ocr(added[0])
        else:
            for ad in added:
                mTesseact.ocr(ad)
    if removed: print ("Removed jpg: ", ", ".join (removed))
    before = after