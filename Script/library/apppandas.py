import pandas as pd



def frame(path=None, cols=None):

    try:
        if path is None:
            return pd.DataFrame()
        if cols is not None:
             return pd.read_spss(path=path, usecols=cols)
        return pd.read_spss(path=path)
    
    except Exception as e:
        raise Exception(e)
