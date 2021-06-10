import pyqrcode
data = input("Enter the link you want to store in QR Image")
image = pyqrcode.create(data)
image.png("image_name.png",scale=8) 