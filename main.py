from  PIL import Image
from pytesseract import pytesseract
import enum


class OS(enum.Enum):
    Mac = 0
    Windows = 1

class Language(enum.Enum):
    ENG = "eng"
    RUS = "rus"
    ITA = "ita"

class ImageReader:
    def __init__(self, os: OS):
        if os == OS.Mac:
            print("Running on macOS\n")
        elif os == OS.Windows:
            windows_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            pytesseract.pytesseract_cmd = windows_path
            print('Running on Windows\n')

    def extract_text(self, image: str, lang: str) -> str:
        print("Opening image:", image)
        img = Image.open(image)
        print("Image opened successfully.")
        print("Extracting text...")
        extracted_text = pytesseract.image_to_string(img, lang=lang)
        print("Text extracted successfully.")
        return extracted_text
        

if __name__ == '__main__':
    ir = ImageReader(OS.Mac)
    text = ir.extract_text('image/i.webp', lang="eng")
    print(text)
