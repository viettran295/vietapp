from pytesseract import pytesseract
from pdf_reader import Pdf_Reader
from translator.translator_app import Translator_App

path_to_pdf = r'C:\Users\viet tran\Desktop\Python\vietapp\dev\files'
pdfs = r"Praktikumszeugnis.pdf"

image = r"Page_1_Praktikumszeugnis.jpg"


reader = Pdf_Reader()
text = reader.img_to_text(image)

# trans = Translator_App('de','en')
# trans_txt = trans.translate_text(text)
# print(trans_txt)