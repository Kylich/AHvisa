import os
import time
import datetime

import mListdir
import mEmail

password_P = '717505021988'

today = datetime.datetime.today().strftime("%Y-%m-%d")
pathToday = os.getcwd() + '\\temp\\%s\\' % today
path_to_watch_P = os.getcwd() + '\\temp\\%s\\pdf\\' % today
path_to_watch_S = os.getcwd() + '\\temp\\%s\\scan\\' % today

if not os.path.exists(pathToday):
    os.makedirs(pathToday)
    os.makedirs(path_to_watch_P)
    os.makedirs(path_to_watch_S)

before_S = dict ([(f, None) for f in os.listdir (path_to_watch_S)])
# before_P = dict ([(f, None) for f in os.listdir (path_to_watch_P)])


while True:
    time.sleep (5)

    mEmail.unseen(path_to_watch_P, password_P)

    mListdir.l(before_S, path_to_watch_S)

    # after_P = dict ([(f, None) for f in os.listdir (path_to_watch_P)])
    # added_P = [f for f in after_P if not f in before_P]
    # removed_P = [f for f in before_P if not f in after_P]
    # for ad_P in added_P:
    #     if '_unprotected' in ad_P:
    #         added_P.remove(ad_P)
    # if added_P:
    #     print ("Added pdf: ", ", ".join (added_P))
    #     if len(added_P)==1:
    #         mPDF.decript(path_to_watch_P, password_P, added_P[0])
    #     else:
    #         for ad_P in added_P:
    #             mPDF.decript(path_to_watch_P, password_P, ad_P)
    # if removed_P: print ("Removed pdf: ", ", ".join (removed_P))
    # before_P = after_P
