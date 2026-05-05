print("let's calculate simple today\nenter any other string to show the result")
x=1
ans=float(input())
while x!=0:
    op=str(input())
    if op=="+":
        num=float(input())
        ans+=num
    elif op=="*":
        num=float(input())
        if ans==0:
            ans=1
        ans*=num
    elif op=="-":
        num=float(input())
        ans-=num
    elif op=="/":
        num=float(input())
        if num==0:
            print('Invalid')
            continue
        ans/=num
    else:
        x=0
print("The answer is ", ans)                