import img2pdf
from PIL import Image
import os
import logging
import yaml
  
def convert(filename):
    print("start")
    with open("config.yaml") as config:
        confdata=yaml.load(config,Loader=yaml.FullLoader)
        jpgPath=confdata['jpgPath']
        pdfPath=confdata['pdfPath']
        logging.info("Converting "+jpgPath+filename+" to "+pdfPath)
        img_path = jpgPath+filename+".jpg"
        pdf_path = pdfPath+filename+".pdf"
        image = Image.open(img_path)
        pdf_bytes = img2pdf.convert(image.filename)
        file = open(pdf_path, "wb")
        file.write(pdf_bytes)
        image.close()
        file.close()
        return "Successfully made pdf file"