import pyqrcode
from pyqrcode import QRCode
import png

url = "www.google.com"

text = pyqrcode.create(url)

text.png('myqr.png', scale=6)
