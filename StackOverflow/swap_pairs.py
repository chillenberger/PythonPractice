'''I want to locate the largest element of r2 and swap it with the element at r2[0,0]. I present the expected output.

import numpy as np
r2 = np.array([[  1.00657843,  63.38075613, 312.87746691],
       [375.25164461, 500.        , 125.75493382],
       [437.6258223 , 250.50328922, 188.12911152]])
indices = np.where(r2 == r2.max())
The expected output is

array([[  500.,  63.38075613, 312.87746691],
       [375.25164461,  1.00657843, 125.75493382],
       [437.6258223 , 250.50328922, 188.12911152]]'''




import numpy as np 


r2 = np.array([[  1.00657843,  63.38075613, 312.87746691],
       [375.25164461, 500.        , 125.75493382],
       [437.6258223 , 250.50328922, 188.12911152]])


r2 = np.append(r2, [[0],[0], [0]], axis=1)
print(r2)