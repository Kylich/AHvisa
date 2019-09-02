import PyPDF2

filename = 'C:\\git\\AHvisa\\NIKITA KULIKOV.pdf'
password = '717505021988'

pdfFile = open(filename, 'rb')
pdfObject = PyPDF2.PdfFileReader(pdfFile)

if pdfObject.decrypt(password) == 1:
    print("Yup, that's it!")
else:
    print('Nope!')