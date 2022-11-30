import img2pdf
from PIL import Image
import os
  
def convert(filename):
    img_path = filename
    pdf_path = "file.pdf"
    image = Image.open(img_path)
    pdf_bytes = img2pdf.convert(image.filename)
    file = open(pdf_path, "wb")
    file.write(pdf_bytes)
    image.close()
    file.close()
    return "Successfully made pdf file"