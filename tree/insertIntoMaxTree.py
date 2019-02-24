"""
998. Maximum Binary Tree II

1. create list first
2. create the tree back from the list

"""

class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
        
        def getList(root):
            
            if not root:
                return []
            
            
            l = []
            r = []

            l = getList(root.left)
            r=  getList(root.right)
            return l + [root.val]+ r
        
        
        t = getList(root) + [val]
        
       
        
        
        def consTree(arr):
            
            
            if arr == []:
                return None
            
            m = arr[0]
            ind = 0
            
            for i,x in enumerate(arr):
                if x >= m:
                    m=x
                    ind = i
            
            root = TreeNode(arr[ind])
            root.left = consTree(arr[:ind])
            root.right = consTree(arr[ind+1:])
            return root

        return consTree(t)
