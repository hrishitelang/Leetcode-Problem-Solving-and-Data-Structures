class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            x = str(x)
            x = x[1:]
            x = x[::-1]
            x = int("-"+x)
        else:
            x = str(x)
            x = int(x[::-1])
            
        # overflow checking
        if -2**31 <= x <= 2**31 - 1:
            return x
        else:
            return 0