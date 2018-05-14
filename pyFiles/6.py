def convert(s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        s1=""
        for row in range(numRows):
            for i in range(row,len(s),2*numRows-2):
                s1+=s[i]
                if row!=0 and row!=numRows-1 and i+2*numRows-2-2*row<len(s):
                    s1+=s[i+2*numRows-2-2*row]
                
        return s1
print(convert("PAYPALISHIRING",3))
             