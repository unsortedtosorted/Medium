class Solution:
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        d={}
        
        temp=head
        
        d[temp]=None
        
        if temp:
            prev=temp
            temp=temp.next
            
        
        
        while temp:
            d[temp]=prev
            prev=temp
            temp=temp.next
        
        last=prev.val
        s=last+1
        
        if s<10:
            prev.val=s
            return head
        else:
            prev.val=s-10
            carry=1
        
        curr=prev
        
        while True:
            curr=d[prev]
            if not curr:
                break
       
            s=curr.val+carry
            if s<10:
                curr.val=s
                return head
            else:
                carry=1
                curr.val=s-10
                prev=curr
        
        if carry!=0:
            temp=ListNode(carry)
            temp.next=head
            return temp
        return head
                
