##
## Agregue una columna  con la suma de _c0 y _c2 a la tabla tbl0.tsv 
## 

import pandas as pd
import numpy as np

x = pd.read_csv('tbl0.tsv', sep='\t')
aux = x.copy()
aux['suma'] = aux['_c0'].astype(int) + aux['_c2'].astype(int)
print(aux)