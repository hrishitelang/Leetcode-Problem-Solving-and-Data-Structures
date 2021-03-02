class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ''
        i = 0
        flag1 = 0
        flag2 = 0
        if len(word1) > len(word2):
            greater = len(word2)
            difference = len(word1) - len(word2)
            flag1 = 1
        elif len(word1) < len(word2):
            greater = len(word1)
            difference = len(word2) - len(word1)
            flag2 = 1
        
        else:
            greater = len(word1)
        
        while i < greater:
            result+=word1[i]
            result+=word2[i]
            i += 1
            
        if flag1:
            result+=word1[-difference:]
        
        if flag2:
            result+=word2[-difference:]
        
            
        return result
        