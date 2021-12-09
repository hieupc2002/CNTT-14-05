print("câu a")
a = [1,1,2,6,8,9,4,5,6,45,34,66,44,37,78]

def kiemtra(n):

    for i in n:
        if i < 30: print(i," ", end=' ')

new_list=(kiemtra(a))
print()
print("câu b")
# câu b
n = int(input("Nhập số để kiểm tra: "))
for i in a:
    if i > n:
        print(i," ", end='')