# Importing Python Modules
from PyPDF2 import PdfReader

path = "example.pdf" # Pdf file path
PDF_Reader = PdfReader(path)

text = ""

# Read the PDF and extract text from all pages
for page_num, page in enumerate(PDF_Reader.pages):
    text += page.extract_text()

print(text) #Print the extracted text