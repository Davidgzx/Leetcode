
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    length=0
    rstr=""
    for i in range(0,len(s)):
        temp=isHuiwen(s,i-1,i+1)
        s.add(temp)
        if length<len(temp):
            length=len(temp)
            rstr=temp 
            
        temp=isHuiwen(s,i,i+1)
        if length<len(temp):
            length=len(temp)
            rstr=temp
    return rstr           
def isHuiwen(s,i,j):
    if i<0 or j>=len(s) or s[i]!=s[j]:
        return s[i+1:j]
    if s[i]==s[j]:
        return isHuiwen(s,i-1,j+1) 