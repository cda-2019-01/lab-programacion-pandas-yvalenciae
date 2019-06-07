##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c5a
## y _c5b (unidos por ':') de la tabla tbl2.tsv
## 

import pandas as pd
import numpy as np
x = pd.read_csv('tbl2.tsv', sep='\t')
x['lista'] = x[['_c5a','_c5b']].apply(lambda x: ':'.join(map(str,x)), axis=1)
x = x.sort_values('lista')
x1 = x.groupby('_c0')['lista'].apply(lambda x: ','.join(map(str, x))).reset_index()
print(x1)