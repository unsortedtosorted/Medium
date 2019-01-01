class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        l=[]
        def inorder(root,l):
            if root:
                if len(l)<k: inorder(root.left,l)
                l.append(root.val)
                if len(l)<k: inorder(root.right,l)
        
        inorder(root,l)
        
        if k-1<=len(l)-1:
            return l[k-1]
        else:
            return None
