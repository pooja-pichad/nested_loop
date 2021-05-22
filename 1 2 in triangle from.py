# 1
# 2 3
# 4 5 6
# 7 8 9 10




n=int(input("enter a number"))
k=1
i=1
while i<=n:
    j=1
    while j<=i:
        print(k,end=" ")
        j=j+1
        k=k+1
    print()
    i=i+1