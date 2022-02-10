import pyqrcode, sys, base64

# TO OBTAIN THE NETWORK INFO FROM THE HOSH:
# if len(sys.argv) < 2:
#     print("Usage: python3 wifi.py [network] [password]")
#     quit()

# network = sys.argv[1]
# if len(sys.argv) > 2:
#     protocol = "WPA/WPA2"
#     pwd = sys.argv[2]
# else:
#     protocol = "nopass"
#     pwd = ""

network = ''
protocol = 'WPA/WPA2'
pwd = ''

qr = pyqrcode.create(f"WIFI:S:{network};T:{protocol};P:{pwd};;")
png = qr.png(f"{network}.png", scale=5)
