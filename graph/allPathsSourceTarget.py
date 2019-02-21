"""

797. All Paths From Source to Target

For a node:
  add node to path
  if node is target, 
    add to path to result
  visit all neightbors
  remove node from path
  
return result:
  Time : 2^N
  


"""


class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.src = 0
        self.dest = len(graph)-1 
        self.result = []
        
        def visitAllNs(index,path):
            
            path.append(index)
            
            if index == self.dest:
                self.result.append(list(path))
            
            for x in graph[index]:
                
                visitAllNs(x,path)
                
            path.pop()
        
        visitAllNs(0,[])
        
        return self.result
