from collections import *

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.pushq=deque()
        self.popq=deque()
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.pushq.appendleft(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while len(self.pushq)>1:
            temp=self.pushq.pop()
            self.popq.appendleft(temp)
        r=self.pushq.pop()
        
        while len(self.popq)>0:
            temp=self.popq.pop()
            self.pushq.appendleft(temp)
        
        return r
            
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        while len(self.pushq)>1:
            temp=self.pushq.pop()
            self.popq.appendleft(temp)
        r=self.pushq.pop()
        
        while len(self.popq)>0:
            temp=self.popq.pop()
            self.pushq.appendleft(temp)
        self.pushq.appendleft(r)
        return r
        
        
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.pushq)==0
