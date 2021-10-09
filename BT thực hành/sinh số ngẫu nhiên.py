import numpy as np
a = np.random.rand()
b = np.random.rand(4) # Mảng có 1x8 phần tử
c = np.random.rand(2, 3) # Mảng có 2x3 phần tử
 
print("a = ", a)
print("b = ", b)
print("c = ", c)

e = np.random
e.seed(10)
print("e rand: ", e.rand())

g = np.random
g.seed(10)          #co seed giong nhau sinh so giong nhau
print("g rand: ", g.rand())