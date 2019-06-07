##
## Si la columna _c0 es la clave en las tablas tbl0.tsv
## y tbl2.tsv, compute la suma de tbl2._c5b por cada
## valor en tbl0._c1.
## 

import pandas as pd
import numpy as np
x1 = pd.read_csv('tbl0.tsv', sep='\t')
x2 = pd.read_csv('tbl2.tsv', sep='\t')
union =  pd.merge(x1, x2, on='_c0')
q12=  union.groupby('_c5a').agg({'_c5b': np.sum})
print(q12.iloc[:,0])