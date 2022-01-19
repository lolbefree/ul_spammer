import code128
import os
from PIL import Image, ImageDraw, ImageFont

def crate_cert_picture(cert_number,):
    cd = code128.image('{}'.format(cert_number))
    cd.save("{}//{}.png".format(os.getcwd(), cert_number))
    img1 = Image.open(f'{os.getcwd()}//cert.jpg')  # main image
    new_barcode = Image.open("{}//{}.png".format(os.getcwd(), cert_number))

    img1.paste(new_barcode, (50, 950))
    img1.save(f"{os.getcwd()}//img_with_barcode.png")

crate_cert_picture("5559515484")
