import os
import time
import datetime

import mTesseact
import mPDF


path_to_watch_S = os.getcwd() + "\\scan"
before_S = dict ([(f, None) for f in os.listdir (path_to_watch_S)])
path_to_watch_P = '.\\pdf\\' + datetime.datetime.today().strftime("%Y-%m-%d") + '\\'
before_P = dict ([(f, None) for f in os.listdir (path_to_watch_P)])

while 1:
    time.sleep (10)
    after_S = dict ([(f, None) for f in os.listdir (path_to_watch_S)])
    added_S = [f for f in after_S if not f in before_S]
    removed_S = [f for f in before_S if not f in after_S]
    if added_S:
        print ("Added jpg: ", ", ".join (added_S))
        if len(added_S)==1:
            mTesseact.ocr(added_S[0])
        else:
            for ad_S in added_S:
                mTesseact.ocr(ad_S)
    if removed_S: print ("Removed jpg: ", ", ".join (removed_S))
    before_S = after_S

    after_P = dict ([(f, None) for f in os.listdir (path_to_watch_P)])
    added_P = [f for f in after_P if not f in before_P]
    removed_P = [f for f in before_P if not f in after_P]
    for ad_P in added_P:
        if '_unprotected' in ad_P:
            added_P.remove(ad_P)
    if added_P:
        print ("Added pdf: ", ", ".join (added_P))
        if len(added_P)==1:
            pass
            mPDF.decript(path_to_watch_P, '717505021988', added_P[0])
        else:
            pass
            for ad_P in added_P:
                mPDF.decript(path_to_watch_P, '717505021988', ad_P)
    if removed_P: print ("Removed pdf: ", ", ".join (removed_P))
    before_P = after_P