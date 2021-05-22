    #     AAAAA
    #    BBBBB
    #   CCCCC
    #  DDDDD





i=1
while i<=5:
    j=1
    while j<=5-i:
        print(" ",end=" ")
        j=j+1
    k=5
    while k==5:
        print(chr(64+i)*5+""*(i+1))
        k=k+1
    i=i+1

