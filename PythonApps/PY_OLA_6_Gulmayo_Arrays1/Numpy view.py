print("Gulmayo, Shayne Marie F.")
print("3BSIT-1\n")

#Numpy view

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)

