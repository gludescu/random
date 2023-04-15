"""
This Python script extracts text from image files (using OCR) in the current working directory and saves the extracted text in a Word document (docx format).

Dependencies:
- pytesseract
- PIL (Python Imaging Library)
- python-docx

How to use this code:

1. Install the required dependencies:
   pip install pytesseract Pillow python-docx
2. Place the script in a directory containing the image files you want to extract text from.
   Supported image formats: .jpg, .jpeg, .png, .bmp, .gif, .tiff
3. Run the script using the command: python script_name.py
4. The script will create a Word document (output.docx) containing the extracted text from the images.

Code Explanation:

- define get_image_files() to retrieve image files from the current working directory
- define get_text_from_image() to extract text from an image using pytesseract
- define create_docx_document() to save extracted text into a Word document
"""

import os
import pytesseract
from PIL import Image
from docx import Document


def get_image_files():
    image_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff")
    files = [f for f in os.listdir('.') if os.path.isfile(
        f) and f.lower().endswith(image_extensions)]
    files.sort()
    return files


def get_text_from_image(image_path):
    image = Image.open(image_path)
    return pytesseract.image_to_string(image)


def create_docx_document(texts, output_file):
    doc = Document()
    for text in texts:
        if text.strip():
            doc.add_paragraph(text.strip())
        doc.add_page_break()
    doc.save(output_file)


if __name__ == "__main__":
    images = get_image_files()
    texts = []

    for image in images:
        text = get_text_from_image(image)
        texts.append(text)

    output_file = "output.docx"
    create_docx_document(texts, output_file)
    print(f"Text from images saved to {output_file}")
