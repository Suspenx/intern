import pandas as pd



def frame(path=None, cols=None):
    try:
        return pd.read_spss(path=path, usecols=cols)
    except Exception as e:
        raise Exception(e)
