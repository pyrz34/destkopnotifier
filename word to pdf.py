import docx
from pdfkit import from_file

def convert_word_to_pdf(word_file, pdf_file):
    doc = docx.Document(word_file)
    from_file(word_file, pdf_file)

# usage
word_file = "my_word_file.docx"
pdf_file = "my_pdf_file.pdf"
convert_word_to_pdf(word_file, pdf_file)