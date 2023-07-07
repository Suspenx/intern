from functions.get_path import getsav
from library.apppandas import frame
import pandas as pd
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
            data_frame = data_frame[data_frame[column].dtypes == np.dtypes.ObjectDType ]
            print (data_frame)
            #if type == np.dtypes.ObjectDType and column not in ignore:
                #print(col)
                #for value in data_frame[col].iterateitems():
                    #if identify_numb(value):
                        #print('Phone#:',value)
               #print(col)
               #numbers_in_column= filter(lambda numb: re.match('^876',numb),filt)
               #print( list (numbers_in_column)

#function that returns dataframe with filtered values
def get_columns_(data_frame= frame(), new_frame=frame()):
    columns = [data_frame[col] for col in data_frame.columns if data_frame[col].dtypes == np.dtypes.ObjectDType and col not in ignore]
    print (pd.DataFrame(data=columns))
   
    



def get_rows_and_information(data_frame= frame()):
    columns= get_columns_(data_frame= frame)
    return pd.concat([read_rows_under_column(column,data_frame) for column in columns])


            
        
def identify_numb(value):
    phone_pattern = r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$'
    if re.match(phone_pattern,value):
        return value


def processSavFiles(files=None):
    if files is None:
        return
    
    for file in files:
        data_frame = frame(path=file)
        # displays to terminal
        fnames= get_columns_(data_frame=data_frame)
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

