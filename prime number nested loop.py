



i=1
while i<=100:
    j=2
    count=0
    while j<i-1:
        if i%j==0:
            count=count+1
        j=j+1
    if i!=1 and count==0:
        print("its prime number,",i)
    else:
        print("not prime number",i)
    i=i+1

