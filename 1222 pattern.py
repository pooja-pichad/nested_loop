# print pattren like,
#     1
# 2   2    2




num=int(input("enter a number "))
i=1
while i<=num:
    j=1
    while j<=num-i:
        print(" ",end=" ")
        j=j+1
    k=1
    while k<i:
        print(i,end=" ")
        k=k+1
    b=i
    while b>0:
        print(k ,end=" ")
        b=b-1
    print()
    i=i+1
