class Solution(object)
    def smallerNumbersThanCurrent(self, nums)
        
        type nums List[int]
        rtype List[int]
        
        a = []
        for i in nums
            temp = i
            count = 0
            for j in nums
                if j is i
                    pass
                elif j  i
                    count += 1
            
            a.append(count)
        return a
        