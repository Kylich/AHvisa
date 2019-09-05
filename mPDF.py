import os
import time
import win32api
import win32print

def decript(path, psw, name):
    PDFfile_de = path + name[:-4] + '_unprotected.pdf'
    PDFfile = path + name
    
    chdirPR = 'C:\\PPR\\'
    chdirAHvisa = os.getcwd() 
    os.chdir(chdirPR)
    os.system('PDFPasswordRemover.exe /userpassword:"' + psw + '" "' + PDFfile + '"')
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

    try:
        # win32api.ShellExecute(0, 'open', GSPRINT_PATH, '-ghostscript "'+GHOSTSCRIPT_PATH+'" -printer "'+currentprinter+'" "' + PDFfile + '"', '.', 0)
        print('win32print good')
    except:
        print('win32print error')
    return

# import datetime
# import os
# today = datetime.datetime.today().strftime("%Y-%m-%d")
# path = os.getcwd() + '\\temp\\%s\\pdf\\' % today
# decript(path, '717505021988', 'NIKITA KULIKOV.pdf')