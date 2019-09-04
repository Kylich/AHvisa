from PyPDF2 import PdfFileReader, utils
from io import StringIO
import subprocess

input_path = 'E:\\nikita\\GitHub\\AHvisa\\111.pdf'

def decompress_pdf(temp_buffer):
    temp_buffer.seek(0)  # Make sure we're at the start of the file.

    process = subprocess.Popen(['pdftk.exe',
                                '-',  # Read from stdin.
                                'output',
                                '-',  # Write to stdout.
                                'uncompress'],
                                stdin=temp_buffer,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    return StringIO(stdout)

with open(input_path, 'rb') as input_file:
    input_buffer = StringIO(input_file.read())

try:
    input_pdf = PdfFileReader(input_buffer)
except utils.PdfReadError:
    input_pdf = PdfFileReader(decompress_pdf(input_file))