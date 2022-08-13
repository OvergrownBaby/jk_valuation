
# -*- coding: GBK -*-

import pandas as pd
import sys
from pathlib import Path
import re
import numpy as np

folder_path_ = Path(sys.argv[1])
subjects_ = list(sys.argv[2:])

def extract_valuation_of_subject(folder_path, subject_name):
    products = {} #indexed by product
    dates = []
    for product in sorted(Path(folder_path).iterdir()):
        print(product)
        name = re.search('九坤.+号', str(product)).group()
        date = re.search('[0-9]{4}.+日',str(product)).group()
        in_df = pd.read_excel(str(product), index_col=0)
        if date not in dates:
            dates.append(date)
        try:
            if name not in products:            
                products[name] = [in_df.loc[subject_name, 'Unnamed: 4']]
            else:
                products[name].append(in_df.loc[subject_name, 'Unnamed: 4'])
        except:
            if name not in products:            
                products[name] = [None]
            else:
                products[name].append(None)
        matrix = np.array([products[i] for i in list(products.keys())], dtype=object)
    out_df = pd.DataFrame(matrix, columns = dates, index=products.keys())
    print(out_df)
    return out_df

def extract_valuations(folder_path, subjects):
    print(str(Path(folder_path).parent.absolute()))
    dfs = []
    for subject in subjects:
        dfs.append(extract_valuation_of_subject(folder_path, subject))
    with pd.ExcelWriter(Path(folder_path).parent / 'output.xlsx') as writer:
        for df, subject in zip(dfs, subjects):
            df.to_excel(writer, sheet_name=f'{subject}')

if __name__=='__main__':
    extract_valuations(folder_path_, subjects_)