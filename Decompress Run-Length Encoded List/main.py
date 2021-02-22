class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            x = []
            if i%2 == 0:
                freq = nums[i]
            else:
                val = nums[i]
                x = [val]*freq
                result += x
        
        return result