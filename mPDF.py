def decript(path, psw, name):
    import os
    # from PyPDF2 import PdfFileReader
    import win32print
    import win32api
    import time, datetime

    PDFfile_de = os.getcwd() + path[1:] + name[:-4] + '_unprotected.pdf'
    PDFfile = os.getcwd() + path[1:] + name
    
    chdirPR = 'C:\\PPR\\'
    chdirAHvisa = os.getcwd() 
    os.chdir(chdirPR)
    os.system('PDFPasswordRemover.exe /userpassword:"' + psw + '" "' + PDFfile + '"')
    os.chdir(chdirAHvisa)

    # print('PDFPasswordRemover.exe /userpassword:"717505021988" "' + path + name + '"')
    time.sleep (5)

    # GHOSTSCRIPT_PATH = "C:\\Program Files\\gs\\gs9.27\\bin\\gswin64.exe"
    # # GSPRINT_PATH = "C:\\Program Files\\gs\\gsprint\\gsprint.exe"

    # currentprinter = win32print.GetDefaultPrinter()
    if os.path.exists(PDFfile_de):
        print(PDFfile_de)
    else:
        print('no PDFfile_de')
        print(PDFfile)
    # win32api.ShellExecute(0, 'open', GHOSTSCRIPT_PATH, '-ghostscript "'+GHOSTSCRIPT_PATH+'" -printer "'+currentprinter+'" "' + PDFFile + '"', '.', 0)
    # win32api.ShellExecute(0, 'open', GSPRINT_PATH, '-ghostscript "'+GHOSTSCRIPT_PATH+'" -printer "'+currentprinter+'" "' + PDFFile + '"', '.', 0)