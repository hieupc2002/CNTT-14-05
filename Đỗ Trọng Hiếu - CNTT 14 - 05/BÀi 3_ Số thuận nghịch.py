Ho_Ten = input("Họ và tên : ")
n = input("Nhập số n : ")
#Đỗ Trọng Hiếu - CNTT 14-05
# n = 254

while( n.isnumeric() == False ):
    print("n phải là số nguyên dương!")
    n = input("Nhập số n : ")

n1 = n[::-1]

print(Ho_Ten)

if n == n1:
    print(n1, " là số nghịch đảo!")
else:
    print(n1, " không phải là số nghịch đảo")