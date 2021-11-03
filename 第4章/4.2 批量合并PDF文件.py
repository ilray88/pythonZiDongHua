from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileMerger
src_folder = Path('F:\\代码文件\\第4章\\公告\\')
des_file = Path('F:\\代码文件\\第4章\\公告\\合并后的公告文件.PDF')
if not des_file.parent.exists():
    des_file.parent.mkdir(parents=True)
file_list = list(src_folder.glob('*.pdf'))
merger = PdfFileMerger()
outputPages = 0
for pdf in file_list:
    inputfile = PdfFileReader(str(pdf))
    merger.append(inputfile)
    pageCount = inputfile.getNumPages()
    print(f'{pdf.name}  页数：{pageCount}')
    outputPages += pageCount
merger.write(str(des_file))
merger.close()
print(f'\n合并后的总页数：{outputPages}')
