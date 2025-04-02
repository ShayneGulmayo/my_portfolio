print("Gulmayo, Shayne Marie F.")
print("3BSIT-1\n")

#Joining two 2d arrays along rows (axis=1)

import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2),axis=1)
print(arr)