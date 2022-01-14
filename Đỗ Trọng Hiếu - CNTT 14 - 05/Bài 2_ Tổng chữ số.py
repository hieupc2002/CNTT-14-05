#Cách 1: Chia cho 10 lấy dư nhiều lần

#Cách 2: Dùng chuỗi
n = input("Nhập số n : ")

#Đỗ Trọng Hiếu - CNTT 14-05
# n = 54

tong = 0

while( n.isnumeric() == False ):
    print("n phải là số nguyên dương!")
    n = input("Nhập số n : ")

for i in range(0 , len(n)):
    tong += int(n[i])

print(tong)