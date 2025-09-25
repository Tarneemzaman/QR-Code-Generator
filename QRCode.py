import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

# First QR
qr = qrcode.QRCode(box_size=12, border=4)
qr.add_data("https://www.youtube.com/watch?v=ueZne-LKdNw")
qr.make(fit=True)  # to make the QR big enough to hold all the data, automatically
qrCode = qr.make_image(fill_color="black", back_color="white")
qrCode.save("qrCode.png")

# Second QR
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data("https://net2025.cc/home")
qr.make(fit=True)
qrCode1 = qr.make_image(fill_color="black", back_color="white")
qrCode1.save("qrCode1.png")

# Decoded first QR
var = decode(Image.open("qrCode.png"))
print(var[0].data.decode("ascii"))
