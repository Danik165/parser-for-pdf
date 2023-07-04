import fitz  # PyMuPDF

def read_pdf(file_path):
    pdf_reader = fitz.open(file_path)
    text = ""
    for page_num in range(len(pdf_reader)):
        text += pdf_reader.load_page(page_num).get_text("text")
    print(text)
    return text
