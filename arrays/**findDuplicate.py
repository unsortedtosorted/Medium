class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        prev=nums[0]
        
        for x in range(1,len(nums)):
            curr=nums[x]
            
            if prev==curr:
                return prev
            else:
                prev=curr
