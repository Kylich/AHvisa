import os
from PyPDF2 import PdfFileReader
import win32print
import win32api

# os.chdir(r"C:\\Program Files (x86)\\4dots Software\\Free PDF Password Remover\\")
# os.system('PDFPasswordRemover.exe /userpassword:"717505021988" "D:\\git\\AHvisa\\NIKITA KULIKOV.pdf"')

# os.chdir(r"D:\\git\\AHvisa\\")
# pdf_document = "NIKITA KULIKOV_unprotected.pdf"  
# with open(pdf_document, "rb") as filehandle:  
#   pdf = PdfFileReader(filehandle)
#   info = pdf.getDocumentInfo()
#   # print (info)
#   pages = pdf.getNumPages()
#   # print ("number of pages: %i" % pages)
#   page1 = pdf.getPage(0)
#   # print(page1)
#   print(page1.extractText())

GHOSTSCRIPT_PATH = "C:\\Program Files\\gs\\gs9.27\\bin\\gswin64.exe"
GSPRINT_PATH = "C:\\Program Files\\gs\\gsprint\\gsprint.exe"

# YOU CAN PUT HERE THE NAME OF YOUR SPECIFIC PRINTER INSTEAD OF DEFAULT
currentprinter = win32print.GetDefaultPrinter()

win32api.ShellExecute(0, 'open', GSPRINT_PATH, '-ghostscript "'+GHOSTSCRIPT_PATH+'" -printer "'+currentprinter+'" "NIKITA KULIKOV_unprotected.pdf"', '.', 0)