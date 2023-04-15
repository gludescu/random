"""
This Python script uses the 'pdf2docx' library to convert a PDF file to a DOCX file. To use this script, follow the steps below:

1. Install the 'pdf2docx' library if you haven't already by running pip install pdf2docx.
2. Set the 'input_pdf' variable to the path of the PDF file you want to convert.
3. Set the 'output_docx' variable to the desired path of the output DOCX file.
4. Run the script. The script will convert the PDF file to a DOCX file, and print a message with the names of the input and output files once the conversion is complete.

Example:

- Suppose you have a PDF file named 'my_document.pdf' that you want to convert to a DOCX file named 'my_converted_document.docx'.
- Set 'input_pdf' to 'my_document.pdf' and 'output_docx' to 'my_converted_document.docx'.
- Run the script. After the conversion, the script will print "PDF file 'my_document.pdf' has been converted to DOCX file 'my_converted_document.docx'."

Please note that the pdf2docx library might not be perfect in handling complex PDF layouts, and some formatting might be lost or altered during the conversion process.
"""

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
