from turtle import fillcolor
import qrcode

data = "www.youtube.com.br"

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color='orange',back_color='white')

img.save('D:/JuuHH/Pictures/Saved Pictures')