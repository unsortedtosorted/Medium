class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def generateTree(l,r):
            node=None
            if l<r:
                mid=(l+r)//2
                node=TreeNode(nums[mid])
                node.left=generateTree(l,mid-1)
                node.right=generateTree(mid+1,r)
            if l==r:
                return TreeNode(nums[l])
            return node
        
        return generateTree(0,len(nums)-1)
