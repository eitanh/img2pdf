import img2pdf
from PIL import Image
import os
import logging
import yaml
from os.path import exists
  
def convert(filename):
    print("start")
    with open("config.yaml") as config:
        try:
            filenameonly,file_extension=os.path.splitext(filename)
            confdata=yaml.load(config,Loader=yaml.FullLoader)
            jpgPath=confdata['jpgPath']
            pdfPath=confdata['pdfPath']
            logging.info("Converting "+jpgPath+filename+" to "+pdfPath)
            img_path = jpgPath+filename
            pdf_path = pdfPath+filenameonly+".pdf"
            file_exists = exists(img_path)
            if not file_exists:
                return "1"
            image = Image.open(img_path)
            pdf_bytes = img2pdf.convert(image.filename)
            file = open(pdf_path, "wb")
            file.write(pdf_bytes)
            image.close()
            file.close()
            return "0"
        except:
            return "1"