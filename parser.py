import pdfplumber
import re


# Function to convert a PDF file to text
def pdf_to_text(input_file):
    try:
        # Open the PDF file using pdfplumber
        with pdfplumber.open(input_file) as pdf:
            paragraphs = []
            # Loop through each page in the PDF
            for page in pdf.pages:
                text = page.extract_text()
                paragraphs.extend(text.split("\n"))

            # Find the first line that is not a number
            header_line_count = 0
            for i, p in enumerate(paragraphs):
                if not re.match(r"^\d+$", p.strip()):
                    header_line_count = i
                    break

            # Keep only the lines that are not empty and do not contain only numbers
            paragraphs = [p for p in paragraphs[header_line_count:] if p.strip() and not re.match(r"^\d+$", p.strip())]

            # Join the paragraphs back together into a single string
            combined_text = "\n".join(paragraphs)

            # Replace the "\no" sub-string with an empty string
            combined_text = combined_text.replace("\no\n", "")

            # Replace the header (manual)
            combined_text = combined_text.replace("IRS Records Management Modernization and e-Records Digitization "
                                                  "Support \nREQUEST FOR INFORMATION  ", '')

            # Split the combined text into sentences
            sentences = combined_text.split(".")

            # Apply the check_sentence function to each sentence
            sentences = [check_sentence(sentence) for sentence in sentences]

            # Join the sentences back together into a single string
            combined_text = ".".join(sentences)

            # Return the final combined text
            return combined_text
    except Exception as e:
        print(f"An error occurred while processing the PDF file: {e}")


# Function to add a "*" symbol before a sentence if it contains a "*" character
def check_sentence(sentence):
    if "*" in sentence:
        return "*" + sentence
    return sentence


# Path to the PDF file
pdf_path = "C:\\Users\\RahulKamireddi\\Downloads\\FY24 RFI_Records Modernization and Digitization Support_FINAL " \
           "VERSION1.1671581868902.pdf "

# Convert the PDF to text
text = pdf_to_text(pdf_path)
print(text)
