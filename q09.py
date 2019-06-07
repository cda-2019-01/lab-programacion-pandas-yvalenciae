##
## Construya una tabla que contenga _c1 y una lista
## separada por ':' de los valores de la columna _c2
## para el archivo tbl0.tsv
## 


import pandas as pd
import numpy as np
x = pd.read_csv('tbl0.tsv', sep='\t')
x = x.sort_values('_c2')
x1 = x.groupby('_c1')['_c2'].apply(lambda x: ':'.join(map(str, x))).reset_index()
x1 = x1.rename(index=str, columns={"_c2": "lista","_c1": "_c0"})
print(x1)