import os
import shutil
src_folder = r'D:\0ilraypan\git_jia\《让工作化繁为简用Python实现办公自动化》\\第3章\\要分类的文件\\'
des_folder = r'D:\0ilraypan\git_jia\《让工作化繁为简用Python实现办公自动化》\\第3章\\分类后的文件\\'
files = os.listdir(src_folder)
print(files)
for i in files:
    src_path = src_folder + i
    if os.path.isfile(src_path):
        des_path = des_folder + i.split('.')[-1]
        if not os.path.exists(des_path):
            os.makedirs(des_path)
        shutil.move(src_path, des_path)