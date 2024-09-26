# Importing Python modules
from PyPDF2 import PdfReader
import pyttsx3

path="example.pdf" # Pdf file path

Speaker=pyttsx3.init()
PDF_Reader=PdfReader(path)

text=""

# Read the PDF and extract text from all pages
for page_num, page in enumerate(PDF_Reader.pages):
    text += page.extract_text()
    Speaker.say(text)
    Speaker.runAndWait()
Speaker.stop()

# Save to mp3 file format
Speaker.save_to_file(text,"pdf_book.mp3")
Speaker.runAndWait()