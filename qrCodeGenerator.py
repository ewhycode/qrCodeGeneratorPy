#install libraries needed
#create function which collects a text and converts it to QR code
#save qr code as image
#run function

import qrcode
def generate_qrcode(text):
    qr = qrcode.QRcode(
        version = 1,
        error_correction = qrcode.constants. ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg0001.png")

url = input("Enter your URL: ")
generate_qrcode(url)
