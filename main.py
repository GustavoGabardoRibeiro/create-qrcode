import qrcode

qr = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

img = qrcode.make(qr)

img.save('C:/Users/Gustavo/Desktop/scripts/meuqrcode1.png')