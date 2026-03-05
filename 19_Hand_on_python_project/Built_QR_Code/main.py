# Build a QR Code Generator using Python that allows you to create QR codes for URLs, text, contact details, or any custom data in seconds.


"""We Are Going To Use A Python Library Like Qrcode And Convert Url To qr """

import qrcode
url=input("Enter Your Url:")
filename=input("Filename You Want To save it as:")
filename=filename+".png"

qr=qrcode.make(url)
save=qr.save(filename)