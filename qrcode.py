import qrcode

# Function to generate QR code
def generate_qr(data, filename="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"✅ QR Code saved as {filename}")

# Example usage
if __name__ == "__main__":
    user_input = input("Enter the text or URL to encode in the QR code: ")
    generate_qr(user_input)
