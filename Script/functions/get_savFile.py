import os
import glob

path="C:/Users/vaugh/Desktop/intern/Script/Files"
def getsav():
    files = glob.glob(path + '/**/*.sav', recursive= True)
    return [os.path.basename(filename) for filename in files]




    

    