name=input("enter a name :")
i=len(name)-1
while i>=0:
    print(name.upper()[i]+name.lower()[i]*(i),end="")
    if i!=len(name):
        print("_",end="")
    i=i-1



# name= input("enter a name ")
# i=0
# while i<len(name):
#     print(name.upper()[i]+name.lower()[i]*(i),end="")
#     if i!=len(name):
#         print("_",end="")
#     i=i+1