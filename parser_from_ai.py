import re

from main_parser import text
paragraphs = re.findall(r'\b([1-9]+\.\s*'
                        r'|\([1-9]+\)\s*'
                        r'|[ivxIVX]\. \s*'
                        r'|[ivxIVX][ivxIVX]\. \s*'
                        r'|[ivxIVX][ivxIVX][ivxIVX]\. \s*'
                        r'|\b(?<![a-zA-Z]\)\s) [a-zA-Z]\.\s*)'
                        r'\s*(.*?)(?=\s*\b([1-9]+\.\s*'
                        r'|\([1-9]+\)\s*'
                        r'|\b(?<![a-zA-Z]\)\s) [a-zA-Z]\.\s*'
                        r'|[ivxIVX]+\.))', text, re.DOTALL)


numerical_index = text.find("1. ")
roman_index = text.find(" I.")

if numerical_index < roman_index:
    print("The numerical_index appears first")
elif roman_index < numerical_index:
    print("The roman index appears first")
else:
    print("Neither symbol appears in the text")



for i, paragraph in enumerate(paragraphs):
    if i == len(paragraphs)-1:
        next_paragraph_index = len(text)
    else:
        next_paragraph_index = text.index(paragraphs[i+1][0])
    paragraph_text = paragraph[1].replace('\n', ' ')
    next_paragraph_text = text[len(paragraph[0])+next_paragraph_index:].replace('\n', ' ')
    print(f"{i+1}.{paragraph_text}{next_paragraph_text}\n")
