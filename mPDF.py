def decript(path, psw, name):
    import os
    from PyPDF2 import PdfFileReader
    import win32print
    import win32api
    import time, datetime

    PDFFile = os.getcwd() + path[1:] + name[:-4] + '_unprotected.pdf'
    
    os.chdir(r"C:\\Program Files (x86)\\4dots Software\\Free PDF Password Remover\\")

    os.system('PDFPasswordRemover.exe /userpassword:"' + psw + '" "' + path + name + '"')

    # print('PDFPasswordRemover.exe /userpassword:"717505021988" "' + path + name + '"')
    time.sleep (5)

    GHOSTSCRIPT_PATH = "C:\\Program Files\\gs\\gs9.27\\bin\\gswin64.exe"
    # GSPRINT_PATH = "C:\\Program Files\\gs\\gsprint\\gsprint.exe"

    currentprinter = win32print.GetDefaultPrinter()


    win32api.ShellExecute(0, 'open', GHOSTSCRIPT_PATH, '-ghostscript "'+GHOSTSCRIPT_PATH+'" -printer "'+currentprinter+'" "' + PDFFile + '"', '.', 0)
    # win32api.ShellExecute(0, 'open', GSPRINT_PATH, '-ghostscript "'+GHOSTSCRIPT_PATH+'" -printer "'+currentprinter+'" "' + PDFFile + '"', '.', 0)