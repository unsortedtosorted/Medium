"""
654. Maximum Binary Tree

1. Find index 'm' of max element in the array
2. root = TreeNode(arr[m])
3. root.left = getRoot(arr[0,m])
4. root.right = getRoot(arr[m+1,:])
5. return root 

Runtime : O(N^2)

"""


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        def getRoot(arr):
            
            if len(arr)==1:
                
                return TreeNode(arr[0])
            
            if len(arr)==0:
                return None
            
            
            m = 0
            temp = arr[0]
            
            for i,x in enumerate(arr):
                
                if x > temp:
                    temp = x
                    m = i
            
            
            root = TreeNode(temp)
            root.left = getRoot(arr[0:m])
            root.right = getRoot(arr[m+1:])
            
            return root
    
        return getRoot(nums)
            
