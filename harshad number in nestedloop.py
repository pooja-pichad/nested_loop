i=1
while i<=1000:
    a=i%10
    b=(i//10)%10
    c=(i//10)//10
    d=a+b+c
    if i%d==0:
        print("harshad number",i)
    else:
        print("not harshad number",i)
    i=i+1
