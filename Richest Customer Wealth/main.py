class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxi = 0
        for i in accounts:
            if sum(i) > maxi:
                maxi = sum(i)
        return maxi