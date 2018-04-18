"""
Reduce Image Size with PIL
Nethika Suraweera
04/17/2018
"""
import os
from PIL import Image
import time
import argparse

timestr = time.strftime("%Y_%m_%d-%H_%M_%S")

parser = argparse.ArgumentParser(description='Image Size Reduce with PIL')
parser.add_argument('input_folder_path', type=str, default="large_images", help='Path to the input images folder')

parser.add_argument('--out_path', type=str, default="small_images_" + timestr, help='Path to the output images folder')

parser.add_argument('--width', type=int, default=200, help='output image width')

args = parser.parse_args()


folder_path = args.input_folder_path
image_width = args.width
result_path = args.out_path

if not os.path.exists(result_path):
    os.makedirs(result_path)

ext = (".jpg", ".png", ".jpeg", ".gif", ".bmp")
files = [file for file in os.listdir(folder_path) if file.lower().endswith(ext)]

print ("Converting the size of images:")
for f in files:
    input_path = os.path.join(folder_path,str(f))
    print("   " + input_path)
    input_img = Image.open(input_path)
    
    # calculate image height
    input_width = input_img.width
    input_height = input_img.height
    factor = input_height / input_width 
    image_height = int(factor * image_width)
    
    # resize
    img = input_img.resize((image_width, image_height), Image.ANTIALIAS)
    
    #fix orientation
    if hasattr(input_img, '_getexif'):
        orientation = 0x0112
        exif = input_img._getexif()
        if exif is not None:
            orientation = exif[orientation]
            rotations = {
                3: Image.ROTATE_180,
                6: Image.ROTATE_270,
                8: Image.ROTATE_90
            }
            if orientation in rotations:
                img= img.transpose(rotations[orientation])
            
    
    # save
    filename = os.path.join(result_path, str(f))
    img.save(filename, quality=100)