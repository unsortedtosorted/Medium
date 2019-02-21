"""
950. Reveal Cards In Increasing Order

Simulate the order using a queue


"""


from collections import deque

class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        index = deque(range(len(deck)))
        
        ans = [0]*len(index)
        
        for x in sorted(deck):
            
            ans[index.popleft()] = x
            
            if index:
                index.append(index.popleft())
        
        
        return ans
