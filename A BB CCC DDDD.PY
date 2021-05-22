# A 
# B B 
# C C C


# num=int(input("enter a number "))
# i=1
# while i<=num:
#     j=1
#     while j<=i:
#         print(chr(64+i),end=" ")
#         j=j+1
#     print()
#     i=i+1



num=int(input("enter a number "))
i=1
while i<=num:
    j=1
    while j<=i:
        print(chr(64+i),i,end=" ")
        j=j+1
    k=0
    while k<=num:
        print(chr(64+i),i,end=" ")
        k=k+1
    print()
    i=i+1