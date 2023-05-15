from pdf2docx import Converter


def convert_pdf_to_docx(input_pdf, output_docx):
    # Create a Converter object
    cvt = Converter(input_pdf)

    # Convert the PDF to a DOCX file
    cvt.convert(output_docx, start=0, end=None)

    # Close the converter
    cvt.close()


if __name__ == "__main__":
    input_pdf = 'my_document.pdf'
    output_docx = 'my_converted_document.docx'

    convert_pdf_to_docx(input_pdf, output_docx)
    print(
        f"PDF file '{input_pdf}' has been converted to DOCX file '{output_docx}'.")
