
upper=0
lower=0
special=0
numeric=0
repeat = 0
ok=0
passwd=input("enter the password")

for i in range (0,len(passwd)):
    if(passwd[i].isupper()):
        upper=upper+1
   
    if(passwd[i].islower()):
        lower=lower+1

    if(passwd[i].isnumeric()):
        numeric=numeric+1
if(not(passwd.isalnum())):
   special=special+1
if(upper and lower and special and numeric):
    ok = 1
elif(not(upper)):
    print("Required atleast one uppercase")
elif(not(lower)):
    print("Required atleast one lowercase")
elif(not(special)):
    print("Required atleast one special character")
elif(not(numeric)):
    print("Required atleast one numeric character")


for i in range (0,(len(passwd)-1)):

        if(passwd[i]==passwd[i+1]):
            repeat=1
            print("Same character repeated")

if(repeat==0 and ok==1):
    print("Password accepted")
