from pytesseract import pytesseract
from pdf_reader import Pdf_Reader

path_to_pdf = r'C:\Users\viet tran\Desktop\Python\vietapp\dev\files'
pdfs = r"Praktikumszeugnis.pdf"

image = r"pdf_reader\Page_1_Praktikumszeugnis.jpg"


reader = Pdf_Reader()
text = reader.img_to_text(image)
print(text)
