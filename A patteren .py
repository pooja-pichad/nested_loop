row=0
while row<7:
    column=0
    while column<5:
        if ((column==0 or column==4)and row!=0)or((row==0 or row==3)and(column>0 and column<4)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        column=column+1
    print()
    row=row+1
        