"""
#442
"""
class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r=[]
        for i, x in enumerate(nums):
            ind = nums[i]
            ind = max(ind,-ind)
            location = nums[ind-1]
            if location<0:
                r.append(ind)
            nums[ind-1]=-nums[ind-1]
        
        return r
