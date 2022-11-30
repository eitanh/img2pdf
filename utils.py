import img2pdf
from PIL import Image
import os
  
# Python3 program to convert image to pfd
# using img2pdf library
  
# importing necessary libraries
import img2pdf
from PIL import Image
import os

img_path = "C:/Users/Admin/Desktop/GfG_images/do_nawab.png"
pdf_path = "C:/Users/Admin/Desktop/GfG_images/file.pdf"
image = Image.open(img_path)
pdf_bytes = img2pdf.convert(image.filename)
file = open(pdf_path, "wb")
file.write(pdf_bytes)
image.close()
file.close()
print("Successfully made pdf file")