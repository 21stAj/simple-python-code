# importing all the required modules
import PyPDF2

# creating a pdf reader object
reader = PyPDF2.PdfReader('Downloads')

# print the number of pages in pdf file
print(len(reader.pages))

# print the text of the first page
print(reader.pages[0].extract_text())

