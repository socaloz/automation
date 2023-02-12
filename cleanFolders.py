"""
@purpose: Clean out folders for specific file types
"""
import os

folder = '\path\to\file'
type = input('What extension of files should be deleted (Example".jpg"): ')

for file in os.listdir(folder):
    if not file.endswith(type):
        continue
    files_path = os.path.join(folder,file)
    try:
        if os.path.isfile(files_path) or os.path.islink(files_path):
            os.unlink(files_path)
    except Exception as e:
        print('Error occured: %s'%(e))
