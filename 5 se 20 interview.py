# 5 4 3 2 1
# 10 9 8 7 6
# 15 14 13 12 11



i=1
while i<=20:
    j=i+4
    while j>i-1:
        print(j, end=" ")
        j=j-1
    print()
    i=i+5