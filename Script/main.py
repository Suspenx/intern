from functions.get_path import getsav
from library.apppandas import frame
import csv
import re
get_files = getsav()

def processSavFiles(files=None):
    if files is None:
        return
    
    for file in files:
        print(file)
        data_frame = frame(path=file)
        print(data_frame.head )
        

processSavFiles(files=get_files)


def get_name():
    column_names= data_frame.columns
    names=[]
    for column in column_names:
        name_matches = re.findall()
