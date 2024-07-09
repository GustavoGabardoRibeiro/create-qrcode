import qrcode

qr = 'PROJETO QRCODE'

img = qrcode.make(qr)

img.save('C:/Users/Gustavo/Desktop/scripts/GerarQRCODE.png')
