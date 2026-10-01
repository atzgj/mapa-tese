import qrcode

url = "https://atzgj.github.io/mapa-tese/"   # <-- tu dirección exacta

qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=12,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

imagen = qr.make_image(fill_color="black", back_color="white")
imagen.save("qr-mapa-tese.png")

print("Listo: qr-mapa-tese.png")