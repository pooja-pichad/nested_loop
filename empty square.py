 
# in this question print pattren 
# * * *
# *   *
# * * *


row=int(input("enter a number "))
column=int(input("enter a number "))
i=1
while i<=row:
    j=1
    while j<=column:
        if i==1 or i==row or j==1 or j==column:
            print("*",end=' ')
        else:
            print(" ",end=' ')
        j=j+1
    print()
    i=i+1