import re

class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str1 = s[:len(s)/2]
        str2 = s[(len(s)/2):]
        count1 = 0
        count2 = 0
        # print(str1)
        # print(str2)
        for i in str1:
            if re.findall(r'[AEIOUaeiou]', i):
                count1 += 1
                
        for i in str2:
            if re.findall(r'[AEIOUaeiou]', i):
                count2 += 1
                
        return count1 == count2