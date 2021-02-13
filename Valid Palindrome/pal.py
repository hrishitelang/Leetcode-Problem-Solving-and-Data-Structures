class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = [i for i in s if i.isalnum()]
        string = ''.join(string)
        string = string.lower()
        return string == string[::-1]