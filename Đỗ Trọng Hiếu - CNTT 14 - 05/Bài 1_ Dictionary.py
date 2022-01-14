Ho_Ten = input("Họ và tên : ")
Ten = input("Nhập Tên : ")
n = len(Ten)
#Đỗ Trọng Hiếu

while( n < 1 ):
    print("Tên không được trống!")
    Ten = input("Nhập Tên : ")
    
dic = dict()

dic["Họ và tên"] = Ho_Ten

for i in range( 1 , n + 1):
    dic[i] = i * i
    
    
print(dic)