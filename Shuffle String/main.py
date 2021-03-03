class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        count = 0
        result = ''
        while count < len(indices):
            index = indices.index(count)
            result+=s[index]
            count += 1
        return result
        