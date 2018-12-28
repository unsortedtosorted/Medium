class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        
        
        toVisit=[0]
        visited=set()
        
        while len(toVisit)>0:
            curr=toVisit.pop()
            
            if curr not in visited:
                visited.add(curr)
                for x in rooms[curr]:
                    toVisit.append(x)
        
        
        return len(visited)==len(rooms)
