print("Gulmayo, Shayne Marie F.")
print("3BSIT-1\n")

#Iterating 3d arrays

import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]],
                [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    print(x)
for x in arr:
    for y in x:
        for z in y:
            print(z)