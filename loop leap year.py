

y=int(input("enter a year"))
y1=int(input("enter a y1"))
i=y
while i<y1:
    if i%4==0 and i%100!=0 or i%400==0:
        print(i)
    i=i+1