# Yeh pattern print karo.
# 1 1
# 1 2 2 1
# 1 2 3 3 1  like this






num=int(input("enter a number "))
column=1
while column<=num:
    Row=1
    while Row<=column:
        print(Row,end=" ")
        Row=Row+1
    k=column  
    while k>0:
        print(k,end=" ")
        k=k-1
    print()
    column=column+1