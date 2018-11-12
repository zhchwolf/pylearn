import os
def delete_file_folder(src):
    if os.path.isfile(src):
        try:
            os.remove(src)
            print('os.remove(src)')
        except:
            print('error 1')
    elif os.path.isdir(src):
        for item in os.listdir(src):
            itemsrc = os.path.join(src,item)
            delete_file_folder(itemsrc)
            print('delete_file_folder(itemsrc)')
        try:
            os.rmdir(src)
        except:
            print('error 2')

dirname = r'D:\360Downloads\Apk'
delete_file_folder(dirname)
