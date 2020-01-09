import os
import time
# import win32api
# import win32print
import sqlite3

def decript(path, filename):
    PDFfile_de = path + filename[:-4] + '_unprotected.pdf'
    PDFfile = path + filename
    name, surname = filename[:-4].split(' ')
    print (name, surname)
    conn = sqlite3.connect('SQLvisa.db')
    cursor = conn.cursor()
    sql = "SELECT * FROM clients WHERE surname=? AND name=?"
    cursor.execute(sql, [(surname), (name)])
    r = cursor.fetchone() # or use fetchone()

    psw = r[2][0:4]+r[3]+r[4]+r[5]
    conn.close() # userpassword:"' + psw + '"    /outputfolder:"'+ path + 'un\\"


    chdirPR = 'D:\\Drive\\Prog distr\\PPR\\'
    chdirAHvisa = os.getcwd() 
    os.chdir(chdirPR)

    PPR = 'PDFPasswordRemover.exe /userpassword:"' + psw + '" "' + PDFfile + '"'
    print(PPR)
    os.system(PPR)
    os.chdir(chdirAHvisa)

    time.sleep (5)

    if os.path.exists(PDFfile_de):
        print(PDFfile_de)
        os.remove(PDFfile)
    else:
        print('no PDFfile_de')
        print(PDFfile)

    # GHOSTSCRIPT_PATH = "C:\\Program Files\\gs\\gs9.27\\bin\\gswin64.exe"
    # GSPRINT_PATH = "C:\\Program Files\\gs\\gs9.27\\bin\\gsprint.exe"
    # currentprinter = win32print.GetDefaultPrinter()

    # try:
    #     # win32api.ShellExecute(0, 'open', GSPRINT_PATH, '-ghostscript "'+GHOSTSCRIPT_PATH+'" -printer "'+currentprinter+'" "' + PDFfile + '"', '.', 0)
    #     print('win32print good')
    # except:
    #     print('win32print error')
    # return

# import datetime
# import os
# today = datetime.datetime.today().strftime("%Y-%m-%d")
# path = os.getcwd() + '\\temp\\'  + today + '\\pdf\\'
# decript(path, 'NIKITA KULIKOV.pdf')