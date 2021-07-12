print("fibonacci series")
n=int(int(input("enter the range:")))
a=0
b=1
if n<=0:
    print("incorrect input")
elif n==1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
