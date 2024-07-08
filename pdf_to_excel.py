import os
import fitz  # PyMuPDF
import pandas as pd

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Function to parse resume text into structured data (simplified example)
def parse_resume_text(text):
    # This function should be adjusted based on the format of your resumes
    data = {
        'Name': None,
        'Email': None,
        'Phone': None,
        'Skills': None,
        'Experience': None,
        'Education': None
    }
    
    # Example of simple parsing (assumes certain keywords exist in text)
    lines = text.split('\n')
    for line in lines:
        if 'Name:' in line:
            data['Name'] = line.split('Name:')[-1].strip()
        elif 'Email:' in line:
            data['Email'] = line.split('Email:')[-1].strip()
        elif 'Phone:' in line:
            data['Phone'] = line.split('Phone:')[-1].strip()
        elif 'Skills:' in line:
            data['Skills'] = line.split('Skills:')[-1].strip()
        elif 'Experience:' in line:
            data['Experience'] = line.split('Experience:')[-1].strip()
        elif 'Education:' in line:
            data['Education'] = line.split('Education:')[-1].strip()
    
    return data

# Function to process all PDFs in a folder and save data to a single Excel file
def process_pdfs_to_excel(input_folder, output_excel_path):
    all_data = []

    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(input_folder, filename)
            text = extract_text_from_pdf(pdf_path)
            resume_data = parse_resume_text(text)
            all_data.append(resume_data)
    
    df = pd.DataFrame(all_data)
    df.to_excel(output_excel_path, index=False)

# Example usage
input_folder = 'path/to/your/pdf/folder'  # Replace with the path to your folder containing the PDF resumes
output_excel_path = 'path/to/output.xlsx'  # Replace with the path where you want to save the Excel file
process_pdfs_to_excel(input_folder, output_excel_path)
