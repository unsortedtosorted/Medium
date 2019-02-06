"""
846. Hand of Straights

1. Give a deck of cards and a number W, return True or False if its possible to 
arrange cards in groups of W, with W consequtive numbers.

2. Create a map of cards
3. Sort the cards
4. For each card x, check if values from x+1 till x+w exist
5. if not return False, if they do decrement all by 1

Run Time : Nlog(N)
Space : O(N)


"""




from collections import Counter

class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        l = len(hand)
        c = Counter(hand)
        
        if l%W != 0:
            return False
        
        hand.sort()
        
        for x in hand:
            
            
            if c[x]==0:
                continue
            
            c[x]-=1
            
            for i in range(x+1,x+W):
                if c[i]<=0:
                    return False
                else:
                    c[i]-=1
        return True
