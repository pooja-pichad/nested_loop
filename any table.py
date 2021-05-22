# print any table

a=int(input("enter a number "))
b=int(input("enter a number2 "))
i=a
while i<=b:
    j=1
    while j<= 10:
        print(i,"*",j,"=",(i*j) , end="  ")
        j=j+1
    print( )
    i=i+1