print("Gulmayo, Shayne Marie F.")
print("3BSIT-1\n")

#Summation over an axis

import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2], axis=1)
print(newarr)
