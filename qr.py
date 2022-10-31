import datetime
from PIL import Image
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from qrcode.image.styles.colormasks import VerticalGradiantColorMask

Logo_link = './github.png'
logo = Image.open(Logo_link)

basewidth = 500
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)

QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=32,
    border=2
)
enlace=input()
QRcode.add_data(enlace)
QRcode.make()
QRimg=QRcode.make_image( image_factory=StyledPilImage, color_mask=VerticalGradiantColorMask(), module_drawer=RoundedModuleDrawer()).convert('RGB')
pos = ((QRimg.size[0] - logo.size[0]) // 2,
       (QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)

suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
QRimg.save(f'./output/{suffix}.png')