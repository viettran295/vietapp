from pdf2image import convert_from_path
from PIL import Image
from pytesseract import pytesseract

#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
path_to_img = "Page_1.jpg"

pdfs = r"Praktikumszeugnis.pdf"

def pdf_to_image(pdfs):
    pages = convert_from_path(pdfs, 350)
    i = 1
    for page in pages:
        image_name = "Page_" + str(i) + ".jpg"  
        page.save(image_name, "JPEG")
        i = i+1   
def img_to_text(path_to_tess: str, path_to_img:str):
    pytesseract.tesseract_cmd = path_to_tesseract
    img = Image.open(path_to_img)
    text = pytesseract.image_to_string(img)
    print(text)