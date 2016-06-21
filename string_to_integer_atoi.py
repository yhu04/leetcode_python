class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str == "":
            return 0 
            
        str = str.strip()
        i = 0
        sign = 1
        new = 0
        MaxInt = (1 << 31) - 1
        
        if str[i]=='+':
            i += 1
        elif str[i]=='-':
            i += 1
            sign = -1
            
        for j in range(i,len(str)):
            if str[j]<'0' or str[j]>'9':
                break
            new = new*10 + int(str[j])
            if new > sys.maxint:
                break 
            
        new *= sign
        if new >=MaxInt:
            return MaxInt
        if new < MaxInt * -1 :
            return MaxInt * - 1 - 1 
        return new 
                
