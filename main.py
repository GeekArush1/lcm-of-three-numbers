def lcm(a,b,c):
    while(True):
        if (c%a==0) and (c%b==0):
            return c
        else:
            return lcm(a,b,c+1)
a=int(input())
b=int(input())
if a > b:
    c = a
else:
    c = b
print(lcm(a,b,c))
