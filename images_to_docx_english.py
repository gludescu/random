import os
import pytesseract
from PIL import Image
from docx import Document

def get_image_files():
    image_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff")
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f.lower().endswith(image_extensions)]
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
