import re
data = input("Nhập vào các giá trị: ")

"""
    Đỗ Trọng Hiếu
    1451020292
    CNTT 14 - 05
    30 - 12 - 2002
"""

l = re.findall(r'\d+', data)
t = tuple(l)

print(data)

print(l)
print(t)