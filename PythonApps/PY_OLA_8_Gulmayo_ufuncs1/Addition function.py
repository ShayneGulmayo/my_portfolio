print("Gulmayo, Shayne Marie F.")
print("3BSIT-1\n")

#Addition function

import numpy as np
def myadd(x, y):
    return x+y
myadd = np.frompyfunc(myadd, 2, 1)
print(myadd([1, 2, 3, 4],
            [5, 6, 7, 8]))

