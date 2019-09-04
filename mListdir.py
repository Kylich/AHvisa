import os
import time
import datetime

import mTesseact
import mPDF



import imaplib
import email.message
import datetime
import base64

YA_HOST = "imap.gmail.com"
YA_PORT = 993
YA_USER = "opengamerroller"
YA_PASSWORD = "Gorod4Narodov"



pathPDF = '.\\pdf\\%s\\' % datetime.datetime.today().strftime("%Y-%m-%d")
if not os.path.exists(pathPDF):
    os.makedirs(pathPDF)

path_to_watch_S = os.getcwd() + "\\scan"
before_S = dict ([(f, None) for f in os.listdir (path_to_watch_S)])
path_to_watch_P = '.\\pdf\\%s\\' % datetime.datetime.today().strftime("%Y-%m-%d")
before_P = dict ([(f, None) for f in os.listdir (path_to_watch_P)])

password_P = '717505021988'

while True:
    time.sleep (10)

    # подключились к почте и логинимся
    imap = imaplib.IMAP4_SSL(YA_HOST)
    imap.login(YA_USER, YA_PASSWORD)
    status, select_data = imap.select()
    # nmessages = select_data[0].decode('utf-8')
    # sender = 'donotreply@vfshelpline.com'
    sender = 'kylikov_nikita@mail.ru'

    # от кого письмо
    status, search_data = imap.search(None, 'FROM', sender)

    for msg_id in reversed(search_data[0].split()):
        status, msg_data = imap.fetch(msg_id, '(RFC822)')
    # включает в себя заголовки и альтернативные полезные нагрузки
        mail = email.message_from_bytes(msg_data[0][1])


        if mail.is_multipart():
            filelist = []
            path = './pdf/' + datetime.datetime.today().strftime("%Y-%m-%d") + '/'
            if not os.path.exists(path):
                os.makedirs(path)

            import base64
            for part in mail.walk():
                if part.get_content_maintype() == 'multipart' or part.get('Content-Disposition') is None:
                    continue

                filename = part.get_filename()

                # Find non-ascii filenames and decode

                transfer_encoding = part.get_all('Content-Transfer-Encoding')
                if transfer_encoding and transfer_encoding[0] == 'base64':
                    filename_parts = filename.split('?')
                    filename = base64.b64decode(filename_parts[3]).decode(filename_parts[1])

                content_type = part.get_content_type()
                if filename:
                    # print(content_type)
                    # print(filename)
                    if not os.path.exists(path+filename):
                        if '.pdf' in filename:
                            filelist.append(filename)
                            with open(path+filename, 'wb') as new_file:
                                new_file.write(part.get_payload(decode=True))
                            print('Закачали файл: ', filename)


                    else: print('Файл уже закачан: ', filename)
            break
    imap.expunge()
    imap.logout()

    after_S = dict ([(f, None) for f in os.listdir (path_to_watch_S)])
    added_S = [f for f in after_S if not f in before_S]
    removed_S = [f for f in before_S if not f in after_S]
    if added_S:
        print ("Added jpg: ", ", ".join (added_S))
        if len(added_S) == 1:
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
            mPDF.decript(path_to_watch_P, password_P, added_P[0])
        else:
            for ad_P in added_P:
                mPDF.decript(path_to_watch_P, password_P, ad_P)
    if removed_P: print ("Removed pdf: ", ", ".join (removed_P))
    before_P = after_P