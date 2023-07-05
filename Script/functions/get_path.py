import os
import glob 


def getsav(parent=None, ext=None):
    if ext is None:
        ext = '.sav'

    if parent is None:
        parent="C:/Users/vaugh/Desktop/intern/Script/Files"

    files = glob.glob(parent + '/**/*' + ext, recursive= True)
    return [filename for filename in files]