class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign= -1 if x < 0 else 1
        x=abs(x)
        temp=x
        digit=0
        result=0
        while temp!=0:
            digit=temp%10
            result=result*10+digit
            temp//=10
        result*=sign
        if ((result<-2**31)or(result>2**31-1)):
            return 0
        else:
            return result