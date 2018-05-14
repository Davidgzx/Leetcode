# ds
def longestPalindrome(s):
#     """
#     :type s: str
#     :rtype: str
#     """
#     dic={}
#     length=0
#     rstr=""
#     if len(s)<=2 and isHuiwen(s)==1:
#         return s
#     for i in range(len(s)):
#         if s[i] not in dic:
#             dic[s[i]]=i
#         if s[i] in dic :
#             if length<len(s[dic[s[i]]:i+1]) and isHuiwen(s[dic[s[i]]:i+1]) ==1:
#                 length=len(s[dic[s[i]]:i+1])
#                 rstr=s[dic[s[i]]:i+1]
            
#     return rstr
    length=0
    rstr=""
    if len(s)%2==0:
        for i in range(1,len(s)-1):
            temp=isHuiwen(s,i-1,i+1)
            if length<=len(temp):
                length=len(temp)
                rstr=temp
        return rstr
    else:
        for i in range(1,len(s)-1):
            temp=isHuiwen(s,i,i+1)

            if length<=len(temp):
                length=len(temp)
                rstr=temp
        return rstr           
def isHuiwen(s,i,j):
        if i==0:
            # print(s[i:j+1])
            return isHuiwen(s,i)
        if j==len(s)-1:
            # print(s[i:j])
            return s[i:j]
        if s[i]!=s[j-1]:
            # print(s[i+1:j-1])
            return s[i+1:j-1]
        if s[i]==s[j-1]:
            i=i-1
            j=j+1
            return isHuiwen(s,i,j)  

# print(longestPalindrome("babadada"))
# print(s[int(len(s)/2):int(len(s)/2)+1])
s="abcaa"
print(longestPalindrome(s))