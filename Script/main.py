from functions.get_path import getsav
from library.apppandas import frame
import csv
import re
import numpy as np
from library.Data import ignore
get_files = getsav()

# function returns names, telephone number and address of respondents 
def filter_(data_frame=frame()): 
    filter=[]
    i =0 
    for column in data_frame.columns:
            col= data_frame[column]
            type= col.dtypes
            if type == np.dtypes.ObjectDType and column not in ignore :
               filter=[col]
               print(filter)


            
    
   

def processSavFiles(files=None):
    if files is None:
        return
    
    for file in files:
        data_frame = frame(path=file)
        fnames= filter_(data_frame=data_frame)
        print(fnames)
        

processSavFiles(files=get_files)




#filter_name(data_frame=frame(path=))


def filter_Number(data_frame):
    number=[]
    for column in data_frame.columns:
        for index in data_frame:
            numb= data_frame.loc[index, column]
            if isinstance(numb, int) and len(numb)<=10 :
                number.append(numb)

