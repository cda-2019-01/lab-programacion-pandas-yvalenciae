##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c4
## de la tabla tbl1.tsv
## 

import pandas as pd
import numpy as np
x = pd.read_csv('tbl1.tsv', sep='\t')
x = x.sort_values('_c4')
x1 = x.groupby('_c0')['_c4'].apply(lambda x: ','.join(map(str, x))).reset_index()
x1 = x1.rename(index=str, columns={"_c4": "lista","_c0": "_c0"})
print(x1)