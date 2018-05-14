class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        dic = {}
        temp = 0
        lastAppear = 0
        length = 0
        for i in range(len(s)):
            if s[i] in dic and lastAppear <= dic[s[i]]:
                lastAppear=dic[s[i]]+1
            dic[s[i]] = i
            temp = dic[s[i]] - lastAppear+1
            # print("Current\t"+str(dic[s[i]])+"\tLast\t"+str(lastAppear)+"\tCurrent-last\t"+str(temp))
            length=max(temp,length)
        print("length\t"+str(length))
        return length