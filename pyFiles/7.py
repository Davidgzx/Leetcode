def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    rint=0
    flag=0
    if x<0:
        flag=1
    x=abs(x)
    while x>9:
        rint+=int(x%10)
        rint*=10
        if rint>65535:
            return 0
        x=int(x/10)
    rint+=x
    if flag==1:
        rint=-rint
    return rint

print(reverse(-123))