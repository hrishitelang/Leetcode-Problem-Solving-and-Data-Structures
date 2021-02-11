class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        if not strs:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            strs.sort()
            for i in range(len(strs[0])):
                if strs[0][i] == strs[-1][i]:
                    result += strs[0][i]
                else:
                    break
        
        return result
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        index = 0
        string = ""
        temp = ""
        for i in strs:
            for j in i:
                if string == "":
                    string = j[0]
                elif j[index] == string[index]:
                        temp = j[index]
                break
            if i == strs[-1]:
                index += 1
            string += temp
        '''    