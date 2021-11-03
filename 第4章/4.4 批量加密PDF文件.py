from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter
src_folder = Path('F:\\代码文件\\第4章\\公告\\')
file_list = list(src_folder.glob('*.pdf'))
for pdf in file_list:
    inputfile = PdfFileReader(str(pdf))
    outputfile = PdfFileWriter()
    pageCount = inputfile.getNumPages()
    for page in range(pageCount):
        outputfile.addPage(inputfile.getPage(page))
    outputfile.encrypt('123456')
    des_name = f'{pdf.stem}_secret.pdf'
    des_file = src_folder / des_name
    with open(des_file, 'wb') as f_out:
        outputfile.write(f_out)
