class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxi = max(candies)
        boolean = []
        for i in candies:
            if i < maxi:
                if i + extraCandies >= maxi:
                    boolean.append(True)
                else:
                    boolean.append(False)
            elif i == maxi:
                boolean.append(True)
        return boolean
        