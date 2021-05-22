#           55555
#         444444
#       333333
#     222222
#    111111




a=5
i=1
while i<=5:
    j=1
    while j<=5-i:
        print(" ",end= "")
        j=j+1
    k=5
    while k>=1:
        print(a,end= "")
        k=k-1
    a=a-1
    print()  
    i=i+1
