num=int(input("enter a number"))
i=1
while i<=num:
    j=1
    while j<=num-i:
        print(" ",end="")
        j=j+2
    k=1
    while k<=i:
        print("*",end=" ")
        k=k+2
    print()
    i+=2
i=1
while i<=num:
    j=1
    while j<=i:
        print(" ",end="")
        j=j+2
    k=1
    while k<=num-i:
        print("*",end=" ")
        k=k+2
    print()
    i=i+2