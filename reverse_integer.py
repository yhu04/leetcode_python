class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x>=0:
            sign=1
        else:
            sigh=-1
        
        reverse=0
        temp=abs(x)
        while temp:
            reverse = reverse*10+temp%10
            reverse /= 10
        
        if reverse>2^32:
            return 0
        else:
            return reverse*sign
        
        
