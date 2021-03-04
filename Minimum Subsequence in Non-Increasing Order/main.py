class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        result = [nums.pop()]
        # print(result)
        # print(sum(result))
        while sum(result) <= sum(nums):
            result.append(nums.pop())
        return result
        