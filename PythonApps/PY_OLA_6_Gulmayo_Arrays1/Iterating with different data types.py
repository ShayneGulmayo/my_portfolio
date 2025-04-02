print("Gulmayo, Shayne Marie F.")
print("3BSIT-1\n")

#Iterating with different data types

import numpy as np
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'],
                   op_dtypes=['S']):
    print(x)