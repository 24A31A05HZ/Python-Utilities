import qrcode
from pathlib import Path


def generate_qr_code():
    print("===== QR Code Generator =====")

    data = input("Enter text or URL: ").strip()

    if not data:
        print("Error: Please enter some text or a URL.")
        return

    filename = input(
        "Enter file name (press Enter for 'qrcode.png'): "
    ).strip()

    if not filename:
        filename = "qrcode.png"

    if not filename.lower().endswith(".png"):
        filename += ".png"

    # Get the folder where this Python file is located
    output_folder = Path(__file__).parent

    # Create the complete output path
    output_path = output_folder / filename

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image()

    image.save(output_path)

    print("\nQR code generated successfully!")
    print(f"Saved to: {output_path}")


if __name__ == "__main__":
    generate_qr_code()
