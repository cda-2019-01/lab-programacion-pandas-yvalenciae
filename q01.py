##
## Imprima la cantidad de registros por cada letra 
## de la columna _c1 de la tabla tbl0
## 


import pandas as pd
import numpy as np
x = pd.read_csv('tbl0.tsv', sep='\t')
q01 = x.groupby('_c1').count()['_c0']
print(q01)