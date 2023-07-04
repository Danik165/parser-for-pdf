import pdfplumber
import re

# Path to PDF file
pdf_path = "C:\\Users\\RahulKamireddi\\Downloads\\FY24 RFI_Records Modernization and Digitization Support_FINAL VERSION1.1671581868902.pdf"
pdf_path = "C:\\Users\\RahulKamireddi\\Downloads\Big_RFI.pdf"
#pdf_path = "C:\\Users\\RahulKamireddi\\Downloads\\Basic RFI Template_Archdesk.pdf"
# Initialize pdfplumber object
with pdfplumber.open(pdf_path) as pdf:
    paragraphs = []
    # Extract text from each page
    for page in pdf.pages:
        text = page.extract_text()
        # Remove page numbers using regex
        text = re.sub(r"\n\s*\d+\s*\n", "\n", text)
        paragraphs.extend(text.split("\n"))

    # Keep only the lines that are not empty and do not contain only numbers
    paragraphs = [p for p in paragraphs if p.strip() and not re.match(r"^\d+$", p.strip())]

    # Join the paragraphs back together into a single string
    text = "\n".join(paragraphs)

    # Replace the "\no\n" sub-string with an empty string
    text = text.replace("\no\n", "")

    # Replace the header (manual)
    text = text.replace("IRS Records Management Modernization and e-Records Digitization "
                        "Support \nREQUEST FOR INFORMATION  ", ' ')

    text = text.replace("\n• ", "\n  • ")

    text = text.replace("\n\n", "\n")
    text = text.replace("\n \n", "\n")
# Print the final output
print(text)
