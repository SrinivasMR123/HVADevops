def cube_root(start,nd,e,n):
    print("Value of end",nd)
    while(1):
        mid=((start+nd)//2)
        print(mid)
        if(abs(n-(mid*mid*mid))<e):
            break
        elif((mid*mid*mid)>nd):
            nd=mid
         #   print("inside mid^3>end ",nd)
        elif((mid*mid*mid)<nd):
            start=mid
            print("value of start",start)
    return mid
n= int(input("Enter an integer: "))  # Take input from the user
end=n
start=0

e=0.000001
res=cube_root(start,end,e,n)
print("The cube root of the entered number is:-",res)

        