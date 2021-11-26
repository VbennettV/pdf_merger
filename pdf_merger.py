import sys
import PyPDF2

# This is the pdf merger
inputs = sys.argv[1:]

# merger.append is appending page one after another while page.
# mergePage is combining the contents of the pages together.

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(f"D:\VbennettV\Excel, Powerquery, DAX tutorial\Python Zero to Mastery\pdf_merger\Input\{pdf}")
    merger.write('super.pdf')

pdf_combiner(inputs)

# This is the pdf watermark stamper
# reader = PyPDF2.PdfFileReader(file)
# print(reader.numPages)

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('D:\VbennettV\Excel, Powerquery, DAX tutorial\Python Zero to Mastery\pdf_merger\Input\wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermarked_output.pdf', "wb") as file:
        output.write(file)
