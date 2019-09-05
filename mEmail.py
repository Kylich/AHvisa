import email.message
import datetime
import imaplib
import base64
import os

import mPdf

YA_HOST = "imap.gmail.com"
YA_USER = "opengamerroller"
YA_PASSWORD = "Gorod4Narodov"
YA_PORT = 993

imap = imaplib.IMAP4_SSL(YA_HOST)
imap.login(YA_USER, YA_PASSWORD)

def unseen(path):
    status, select_data = imap.select()
    # sender = 'donotreply@vfshelpline.com'
    # sender = 'kylikov_nikita@mail.ru'
    status, search_data = imap.search(None, 'UNSEEN')
    status=status

    for msg_id in reversed(search_data[0].split()):
        status, msg_data = imap.fetch(msg_id, '(RFC822)')
        mail = email.message_from_bytes(msg_data[0][1])

        if mail.is_multipart():
            for part in mail.walk():
                if part.get_content_maintype() == 'multipart' or part.get('Content-Disposition') is None:
                    continue

                filename = part.get_filename()

                transfer_encoding = part.get_all('Content-Transfer-Encoding')
                if transfer_encoding and transfer_encoding[0] == 'base64':
                    filename_parts = filename.split('?')
                    filename = base64.b64decode(filename_parts[3]).decode(filename_parts[1])

                # content_type = part.get_content_type()
                if filename:
                    if not os.path.exists(path+filename) or \
                       not os.path.exists(path+filename[:-4] + '_unprotected.pdf'):
                        if '.pdf' in filename:
                            with open(path+filename, 'wb') as new_file:
                                new_file.write(part.get_payload(decode=True))
                            print('Закачали файл: ', filename)
                        mPdf.decript(path, filename)    
                    else: print('Файл уже закачан: ', filename)
            break