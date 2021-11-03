from pathlib import Path
from filecmp import cmp
src_folder = Path('F:\\代码文件\\第3章\\图片\\')
des_folder = Path('F:\\代码文件\\第3章\\图片\\重复的图片\\')
if not des_folder.exists():
    des_folder.mkdir(parents=True)
result = list(src_folder.glob('*'))
file_list = []
for i in result:
    if i.is_file():
        file_list.append(i)
for m in file_list:
    for n in file_list:
        if m != n and m.exists() and n.exists():
            if cmp(m, n):
                n.replace(des_folder / n.name)

