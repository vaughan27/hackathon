import PyPDF2
 
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        num_pages = len(reader.pages)
        text = []
        for page_number in range(num_pages):
            page = reader.pages[page_number]
            page_text = page.extract_text()
            text.append(page_text)
        return '\n'.join(text)

text = extract_text_from_pdf('resume.pdf')

