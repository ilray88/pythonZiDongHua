from pathlib import Path
src_folder = Path('F:\\代码文件\\第3章\\要分类的文件\\')
des_folder = Path('F:\\代码文件\\第3章\\分类后的文件\\')
files = src_folder.glob('*')
for i in files:
    if i.is_file():
        des_path = des_folder / i.suffix.strip('.')
        if not des_path.exists():
            des_path.mkdir(parents=True)
        i.replace(des_path / i.name)