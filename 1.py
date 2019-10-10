from PyPDF2 import PdfFileReader
import os


f = open('pdfs\\1.pdf', 'rb')
content = ""
read_pdf = PdfFileReader(f)
for i in range(read_pdf.getNumPages()):
    page = read_pdf.getPage(i)
    #print ('Page No - ' + str(1+read_pdf.getPageNumber(page)))
    page_content = page.extractText()
    #print(page_content)
    content += page_content


f.close()

print(content)