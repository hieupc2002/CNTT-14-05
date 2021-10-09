import numpy as np
print("Trung bình mặt ngửa 20 lần ",np.random.binomial(20, 0.5))
 # Số mặt ngửa nhận được khi tung đồng xu 10 lần
print("Trung bình mặt ngửa 20 lần trong vòng 10 lần lặp: ",np.random.binomial(20, 0.5, 10))
print("trung bình : ",np.random.binomial(20, 0.5, 10).mean())
 # Số mặt ngửa nhận được khi tung đồng xu 20 lần trong 10 lần lặp
