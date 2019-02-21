""""
814. Binary Tree Pruning

For root:
  
  1. if left subtree has 1, keep it , other wise delete
  2. if right subtree has 1, keep it, otherwise delete
  3. return true if right subtree or left subtree or root has 1
  
  Run time : ON)
  space : O(H) 

""""


class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def checkOne(root):
            l = False
            r = False
            if root:
                
                if not root.left and not root.right:
                    if root.val == 1:
                        return True
                    else:
                        return False
                
                l  =  checkOne(root.left)
                r  =  checkOne(root.right)
                
                if root.left:
                    if not l:
                        root.left = None
                if root.right:
                    if not r:
                        root.right = None
                
                return l or r or root.val == 1
        
        if checkOne(root):
            return root
        else:
            return None
