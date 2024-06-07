import qrcode

# URL locale de votre fichier HTML
url = "file:///Users/mac/Desktop/scan%20app/Switch_1.html"

# Générer le code QR
img = qrcode.make(url)

# Sauvegarder l'image dans un fichier
img.save("switch_1_qr.png")

print("QR code generated and saved as switch_1_qr.png")
