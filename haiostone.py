def hailstone(num):
    list=[]
    len=0
    if(num<0):
        return 1
    while(num>1):
        if(num%2==0):
            num=num/2
        else:
            num=num*3+1
        len=len+1
        list.append(num)
    return ((list,len))
print(hailstone(56))
