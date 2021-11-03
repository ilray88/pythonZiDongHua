from pathlib import Path
import win32com.client as win32
src_folder = Path('F:\\代码文件\\第5章\\要替换关键词的合同文件\\')
des_folder = Path('F:\\代码文件\\第5章\\替换关键词后的合同文件\\')
if not des_folder.exists():
    des_folder.mkdir(parents=True)
file_list = list(src_folder.glob('*.docx'))
replace_dict = {'中酿': '中亮', '订立': '签订'}
word = win32.gencache.EnsureDispatch('Word.Application')
word.Visible = False
cs = win32.constants
for i in file_list:
    doc = word.Documents.Open(str(i))
    print(i.name)
    for old_txt, new_txt in replace_dict.items():
        findobj = word.Selection.Find
        findobj.ClearFormatting()
        findobj.Text = old_txt
        findobj.Replacement.ClearFormatting()
        findobj.Replacement.Text = new_txt
        if findobj.Execute(Replace=cs.wdReplaceAll):
            print(f'{old_txt}-->{new_txt}')
    new_file = des_folder / i.name
    doc.SaveAs(str(new_file))
    doc.Close()
word.Quit()
