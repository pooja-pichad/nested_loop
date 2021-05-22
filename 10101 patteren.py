# 1 0 1 0 1 0 1
#   1 0 1 0 1
#     1 0 1
#       1



i=7
while i>=1:
    k=6
    while k>=i:
        print("",end=" ")
        k=k-1
    j=1
    while j<=i:
        if j%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")
        j=j+1
    i=i-2
    print()

# Sorting the list.

# list1 = [7,46,8,1,10]
# i = 0
# while i<len(list1):
#     j = 0
#     while j<len(list1)-1:
#         if list1[j+1] < list1[j]:
#             list1[j], list1[j+1] = list1[j+1], list1[j]
#         j += 1
#     i += 1
# print(list1)
