n = input("Nhập số n : ")

#Đỗ Trọng Hiếu - CNTT 14-05
# n = 254

while( n.isnumeric() == False ):
    print("n phải là số nguyên dương!")
    n = input("Nhập số n : ")

n1 = n[::-1]

if n == n1:
    print("Đây là số nghịch đảo!")
else:
    print("Đây không phải là số nghịch đảo")

print(n1)