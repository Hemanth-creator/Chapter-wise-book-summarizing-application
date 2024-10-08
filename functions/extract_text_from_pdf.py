# function to extract text from pdf using fitz
import fitz

def extract_text_from_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path)
    full_text = ""
    
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        full_text += page.get_text()
    
    pdf_document.close()
    return full_text