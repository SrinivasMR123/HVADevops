def balancepar(testVariable,startindex,currindex):
    open = 0
    close = 0
    for i in range(len(testVariable)):
        if(testVariable[i] == '('):
            open+=1
        elif(testVariable[i] == ')'):
            close += 1
        else:
            return -1
        currindex +=1
    if(open == close):
        return 0
    else:
        return 1

testVariable = list(map(str,input("Enter the array values:").split()))
a = balancepar(testVariable,0,0)
if(a == 0):
    print("The brackets are balanced")
elif(a == 1):
    print("The brackets are not balanced")
else:
    print("Please use only '(' or ')'")