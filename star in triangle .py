# print pattern STAR in triangle

# num=int(input("enter a number "))
# i=1
# while i<=num:
#     j=1
#     while j<=num-i:
#         print(" ",end=" ")
#         j=j+1
#     k=1
#     while k<i:
#         print("*",end=" ")
#         k=k+1
    # b=i
    # while b>0:
    #     print("*",end=" ")
    #     b=b-1
    # print()
    # i=i+1


i=1
while i<=5:
    b=1
    while b<=5-i:
        print("",end=" ")
        b=b+1
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    print()
    i=i+1
