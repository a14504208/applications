import shutil, os

src_dir = r'C:\Users\Louis\Desktop\18-02-fall-2007'
dest_dir = r'C:\Users\Louis\Desktop\extracted'

for (root, sub_dirs, files) in os.walk(src_dir):
    for sub_dir in sub_dirs:
        dir_path = dest_dir + '\\' + sub_dir
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        
    for file in files:
        if file.endswith('.pdf'):
            src_path = root + '\\' + file
            dest_path = dest_dir + root[len(src_dir):]
            shutil.copy(src_path, dest_path)

for (root, sub_dirs, files) in os.walk(dest_dir):
    for sub_dir in sub_dirs:
        dir_path = dest_dir + '\\' + sub_dir
        if os.path.getsize(dir_path) == 0:
            shutil.rmtree(dir_path)


