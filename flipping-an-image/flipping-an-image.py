class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        image = [i[::-1] for i in image]
        return [[0 if val==1 else 1 for val in i] for i in image]