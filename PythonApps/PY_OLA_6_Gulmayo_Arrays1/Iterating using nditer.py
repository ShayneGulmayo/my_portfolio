print("Gulmayo, Shayne Marie F.")
print("3BSIT-1\n")

#Iterating using nditer

import numpy as np
arr = np.array([[[1, 2], [3, 4]],
                [[5, 6], [7, 8]]])
for x in np.nditer(arr):
    print(x)