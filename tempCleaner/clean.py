import os
import shutil

temp_path = os.getenv('Temp')

try:
    with os.scandir(temp_path) as archive:
        
            for item in archive:
                try:
                    if item.is_symlink() or item.is_junction():
                         print('Ignored link or junction :',item.name)

                    elif item.is_file():
                        os.remove(item.path)
                        print('File removed successfully')

                    elif item.is_dir():
                        shutil.rmtree(item.path)
                        print('Folder removed successfully')

                except OSError as e:
                    print(e)

except OSError as e:
    print(e)