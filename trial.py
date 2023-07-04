import PyPDF4
import mysql.connector
import nltk

nltk.download('punkt')
from nltk.tokenize import sent_tokenize


def read_pdf_1(file_path):
    with open(file_path, "rb") as file:
        pdf_reader = PyPDF4.PdfFileReader(file)
        text = ""
        for page_num in range(pdf_reader.numPages):
            text += pdf_reader.getPage(page_num).extractText()

    return text
import fitz  # PyMuPDF

def read_pdf(file_path):
    pdf_reader = fitz.open(file_path)
    text = ""
    for page_num in range(len(pdf_reader)):
        text += pdf_reader.load_page(page_num).get_text("text")
    print(text)
    return text

def tokenize_text(text):
    return sent_tokenize(text)


def filter_questions(sentences):
    questions = [sentence for sentence in sentences if '?' in sentence]
    return questions


def connect_to_database(host, user, password, database):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database="pdf"
    )

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        question_text TEXT
    );
    """)

    cursor.close()

    return connection


def save_questions_to_database(connection, questions):
    cursor = connection.cursor()
    query = "INSERT INTO questions (question_text) VALUES (%s)"
    for question in questions:
        cursor.execute(query, (question,))
    connection.commit()
    cursor.close()


def main():
    file_path = "C:\\Users\\RahulKamireddi\\Downloads\\Big_RFI.pdf"
    text = read_pdf(file_path)
    sentences = tokenize_text(text)
    questions = filter_questions(sentences)

    host = 'localhost',
    user = 'root',
    password = '1234',
    database = "pdf"
    connection = connect_to_database(host, user, password, database)

    save_questions_to_database(connection, questions)
    connection.close()


if __name__ == "__main__":
    main()
