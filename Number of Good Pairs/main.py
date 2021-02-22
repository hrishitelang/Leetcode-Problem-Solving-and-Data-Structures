class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = []
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i != j:
                    if nums[i] == nums[j] and i < j:
                        temp.append((i, j))
        # print(temp)
        return len(temp)