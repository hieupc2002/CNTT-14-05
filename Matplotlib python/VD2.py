import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
y=x**3
plt.plot([1,2,3,4],[1,4,9,16],"green",x,y,"yellow")
plt.title("First Plot")
plt.xlabel("Truc X")
plt.ylabel("Truc y")
plt.show()