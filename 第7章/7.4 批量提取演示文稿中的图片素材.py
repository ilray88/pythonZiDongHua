from pathlib import Path
from zipfile import ZipFile
import win32com.client as win32
def ppt2pptx(ppt_path):
    ppt_app = win32.gencache.EnsureDispatch('PowerPoint.Application')
    ppt = ppt_app.Presentations.Open(ppt_path)
    pptx_path = ppt_path.with_suffix('.pptx')
    ppt.SaveAs(pptx_path, 24)
    ppt.Close()
    ppt_app.Quit()
    return pptx_path
def extract_img(ppt_path, img_folder):
    if ppt_path.suffix == '.ppt':
        ppt_path = ppt2pptx(ppt_path)
    with ZipFile(ppt_path) as zf:
        for name in zf.namelist():
            if name.startswith('ppt/media/image'):
                zf.extract(name, img_folder)
pptx_file = Path('F:\\代码文件\\第7章\\PPT模板.pptx')
img_folder = Path('F:\\代码文件\\第7章\\图片素材\\')
if not img_folder.exists():
    img_folder.mkdir(parents=True)
extract_img(pptx_file, img_folder)
