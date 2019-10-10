import PyPDF2
import pandas as pd 

def pdf2csv(pdfName):
    
    read_pdf = PyPDF2.PdfFileReader(pdfName)
    content = ""
    for i in range(read_pdf.getNumPages()):
        page = read_pdf.getPage(i)
        page_content = page.extractText()
        content += page_content
    content= content.replace('\n',' ')
    print(content.split('.'))

    list_sentences = content.split('.')#sent_tokenize(content)

    df = pd.DataFrame(list_sentences)
    df['name'] = pdfName

    cols = df.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    df = df[cols]

    df.to_csv("csv\\{0}.csv".format(pdfName))
    print(df)

#pdf2csv('pdfs\\1.pdf')

import os

arr = os.listdir('pdfs')

for i in range(len(arr)):
    print(arr[i])
    pdf2csv('pdfs\\'+arr[i])



import glob

os.chdir("csv\\pdfs")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
