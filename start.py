from pdf2docx import Converter
import PyPDF2

file_name = "C:\\Users\\RahulKamireddi\\Downloads\\Big_RFI.pdf"

import cloudconvert

cloudconvert.default()

converter = Converter()
converter.convert(file_name)
