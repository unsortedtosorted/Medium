class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True
        l=[root]
        val=root.val
        while len(l)>0:
            temp=l.pop()
            if not temp:
                continue
            if temp.val!=val:
                return False
            else:
                l.append(temp.left)
                l.append(temp.right)
        return True
                
