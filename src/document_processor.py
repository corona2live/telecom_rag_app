import os
import PyPDF2

def extract_text_from_pdfs(pdf_dir):
    text_data = []
    for filename in os.listdir(pdf_dir):
        if filename.endswith('.pdf'):
            with open(os.path.join(pdf_dir, filename), 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                text = " ".join([page.extract_text() for page in reader.pages if page.extract_text()])
                text_data.append((filename, text))
    return text_data
