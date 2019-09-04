import os
from PyPDF2 import PdfFileReader

# os.chdir(r"C:\\Program Files (x86)\\4dots Software\\Free PDF Password Remover\\")
# os.system('PDFPasswordRemover.exe /userpassword:"717505021988" "D:\\git\\AHvisa\\NIKITA KULIKOV.pdf"')

os.chdir(r"D:\\git\\AHvisa\\")
pdf_document = "NIKITA KULIKOV_unprotected.pdf"  
with open(pdf_document, "rb") as filehandle:  
  pdf = PdfFileReader(filehandle)
  info = pdf.getDocumentInfo()
  # print (info)
  pages = pdf.getNumPages()
  # print ("number of pages: %i" % pages)
  page1 = pdf.getPage(0)
  # print(page1)
  print(page1.extractText())