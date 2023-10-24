from PIl import Image
import cv2
import matplotlib.pyplot as plt
from utils import in_file, out_file

def grayscale(colored):
    w,h = colored.size
    img = Image.new("RGB",(w,h))

    for x in range (w):
      for y in range (h):
         pxl = colored.getpixel((x,y))
         lum =(pxl[0]+pxl[1]+pxl[2])//3
         img.putpixel((x,y),(lum,lum,lum))
         return img



if __name__ == "__main__":
    img = Image.open(in_file("Screenshot.jpg"))
 
    grayscale(img).save(out_file("pb-Screenshot.jpg"))
    