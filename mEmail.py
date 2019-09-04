import imaplib
import email.message
import os.path
import datetime
import base64

import mPDF

YA_HOST = "imap.gmail.com"
YA_PORT = 993
YA_USER = "opengamerroller"
YA_PASSWORD = "Gorod4Narodov"

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



