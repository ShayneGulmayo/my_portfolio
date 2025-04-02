print("Gulmayo, Shayne Marie F.")
print("3BSIT-1\n")

#Check if function is a ufunc

import numpy as np
print(type(np.add))
if type(np.add) == np.ufunc:
    print('add is ufunc')
else:
    print('add is not ufunc')
    