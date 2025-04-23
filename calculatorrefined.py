def x(s):
    d=0
    for c,h in enumerate(s[::-1]):
        if h!='1'and h!='0':return'E'
        if h=='1':d+=2**c
    return d
def bc(l,u,o):
    1=x(l)
    2=x(u)
    if 1=='E'or 2=='E':return'E'
    if o=='/':
        if 2==0:return'N'
        else:t=1/2
    elif o=='+':t=1+2
    elif o=='-':t=1-2
    elif o=='*':t=1*2
    if t>255 or t<0:return'F'
    g=''
    z=int(t).bit_length()
    for i in range(z-1,-1,-1): 
        p=2**i
        if g>=p: 
            g+='1' 
            g-=p
        else:
            g+='0'
    return g.rjust(8,'0') 