from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
divisions = ['Div-A','Div-B','Div-C','Div-D','Div-E']
Lua = [70,82,73,65,68]
#variance = [50,8,7,6,4]
Gao = [68,67,72,61,46]

index = np.arange(5)
width = 0.3

plt.bar(index,Lua, width ,color='red',label = 'Gạo')#plt.barh bieeu do ngang     xerr ngang(yerr =variance)
plt.bar(index,Gao, width,color='blue',label = 'Lúa',bottom=Lua)#yerr =variance 
plt.title("Bieu do 2 cot ")
plt.ylabel("Divisions")
plt.xlabel("Marks")
plt.xticks(index,divisions)
plt.legend(loc='best')
plt.show()