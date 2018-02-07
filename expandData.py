from astropy.table import Table, Column, vstack
import numpy as np
tab = Table.read('tableDiff.csv', fill_values=[('nan','')])

btab = vstack([tab,tab])
for i in range(5):
    btab = vstack([btab,tab])

ind = np.arange(1,len(btab)+1)
c = Column(data=ind, dtype=np.dtype('u4'), name="index")
btab.add_column(c, index=0)

btab.write("tableDiffBig.csv", overwrite=True)