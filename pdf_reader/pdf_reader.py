from pdf2image import convert_from_path
from PIL import Image
from pytesseract import pytesseract
from fpdf import FPDF
from typing import List



class Pdf_Reader:
    #Define path to tessaract.exe (OCR - optical character recognition engine)
    path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    @staticmethod       
    def pdf_to_img(path_to_pdf: str, pdfs: str):
        pages = convert_from_path(path_to_pdf+"/"+pdfs, 350)
        i = 1
        for page in pages:
            img_name = "Page_" + str(i) + "_" + pdfs[:-4] + ".jpg"  
            page.save(img_name, "JPEG")
            i = i+1   

    def img_to_text(self, path_to_img) -> str:
        pytesseract.tesseract_cmd = self.path_to_tesseract
        img = Image.open(path_to_img)
        return pytesseract.image_to_string(img)

    @staticmethod
    def text_to_pdf(text: str, img_name: str):
        pdf = FPDF()
        pdf.set_font("Arial", size=15)
        pdf.add_page()
        pdf.cell(200,10,txt=text)
        pdf.output(img_name, "F")


if __name__ == "__main__":
    img = "Page_1_Praktikumszeugnis.jpg"
    reader = Pdf_Reader()
    txt = reader.img_to_text(img)
    print(txt)