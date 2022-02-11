import pyqrcode, sys, base64

network = ''
protocol = 'WPA/WPA2'
pwd = ''

qr = pyqrcode.create(f"WIFI:S:{network};T:{protocol};P:{pwd};;")
png = qr.png(f"{network}.png", scale=5)
