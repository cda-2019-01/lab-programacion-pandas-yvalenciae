##
## Imprima los valores unicos e la columna _c4 de 
## de la tabla tbl1 en mayusculas
## 

import pandas as pd
import numpy as np

x1 = pd.read_csv('tbl1.tsv', sep='\t')
l= x1['_c4'].unique()
q04 = [x.upper() for x in l]
q04.sort()
print(q04)