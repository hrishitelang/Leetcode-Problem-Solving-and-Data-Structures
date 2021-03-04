class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitude = []
        altitude.append(0)
        for i in range(1, len(gain)+1):
            altitude.append(altitude[i-1] + gain[i-1])
        return max(altitude)