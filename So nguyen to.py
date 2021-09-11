a = int(input())
flag = True
if a<2:
    flag = False
elif a==2:
    flag = True
elif a%2==0:
    flag = False
else:
    for i in range(3 ,a , 2):
        if a%i==0:
            flag = False
if flag == True:
    print( a , " là số nguyên tố")
else:
    print( a , " không là số nguyên tố")