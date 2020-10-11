import pyqrcode
import png
# Import QRCode from pyqrcode 
from pyqrcode import QRCode 


# String which represents the QR code 
s = int(9876543210)

# Generate QR code 
url = pyqrcode.create(s) 

# Create and save the svg file naming "myqr.svg" 
url.svg("Phone.svg", scale = 8) 

# Create and save the png file naming "myqr.png" 
url.png('Phone.png', scale = 8) 
