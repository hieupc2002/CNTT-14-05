n = int(input("Nhap n : "))

#Đỗ Trọng Hiếu

while( n < 1 ):
    print("n phải lớn hơn 0")
    n = int(input("Nhap n : "))
    
dic = dict()

for i in range( 1 , n + 1):
    dic[i] = i * i

print(dic)