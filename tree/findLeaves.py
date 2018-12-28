class Solution:
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root:
            return []
        
        
        def getleaves(root):
            
            if root:
                lleaves=[]
                rleaves=[]                
                if root.left==None and root.right==None:
                    return ([root.val],True)
                deleltel=False
                delelter=False
                if root.left:
                    lleaves,deleltel=getleaves(root.left)
                if root.right:
                    rleaves,delelter=getleaves(root.right)
                if deleltel:
                    root.left=None
                if delelter:
                    root.right=None
                return (lleaves+rleaves,False)
        
        r=[]
        
        while root.left!=None or root.right!=None:
            r.append(getleaves(root)[0])
                
        r.append([root.val]) 
        root=None
        return (r) 
