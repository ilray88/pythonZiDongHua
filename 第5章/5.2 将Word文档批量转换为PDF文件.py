from pathlib import Path
from comtypes.client import CreateObject
src_folder = Path('F:\\代码文件\\第5章\\合同文件\\')
des_folder = Path('F:\\代码文件\\第5章\\PDF文件\\')
if not des_folder.exists():
    des_folder.mkdir(parents=True)
file_list = list(src_folder.glob('*.docx'))
word = CreateObject('Word.Application')
for word_path in file_list:
    pdf_path = des_folder / word_path.with_suffix('.pdf').name
    if pdf_path.exists():
        continue
    else:
        doc = word.Documents.Open(str(word_path))
        doc.SaveAs(str(pdf_path), FileFormat=17)
        doc.Close()
word.Quit()