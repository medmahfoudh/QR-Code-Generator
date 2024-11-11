# Python Code QR Generator

import qrcode
from PIL import Image 

def generate_qr_code(data, file_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)

def display_qr_code(file_path):
    img = Image.open(file_path)
    img.show()

if __name__ == "__main__":
    data_to_encode = input("Enter the data you want to encode: ")
    output_file_path = input("Enter the output file path (e.g., 'my_qrcode.png'): ")

    generate_qr_code(data_to_encode, output_file_path)
    print(f"QR code saved to {output_file_path}")

    display_option = input("Do you want to display the QR code? (y/n): ").lower()
    if display_option == 'y':
        display_qr_code(output_file_path)
        