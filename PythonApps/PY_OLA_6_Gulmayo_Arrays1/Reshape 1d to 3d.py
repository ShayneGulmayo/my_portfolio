print("Gulmayo, Shayne Marie F.")
print("3BSIT-1\n")

#Reshape 1d to 3d

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7,
                8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)