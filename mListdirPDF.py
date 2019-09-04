import os
import time
import datetime
import mPDF

path_to_watch = './pdf/' + datetime.datetime.today().strftime("%Y-%m-%d") + '/'
before = dict ([(f, None) for f in os.listdir (path_to_watch)])
while 1:
    time.sleep (10)
    after = dict ([(f, None) for f in os.listdir (path_to_watch)])
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]
    print(added)
    for ad in added:
        if '_unprotected' in ad:
            added.remove(ad)
    if added:
        print ("Added: ", ", ".join (added))
        if len(added)==1:
            pass
            mPDF.decript(path_to_watch, 'passw', added[0])
        else:
            pass
            for ad in added:
                mPDF.decript(path_to_watch, 'passw', ad)
    if removed: print ("Removed: ", ", ".join (removed))
    before = after