class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        i=[0]
        def search(l,r):
            
            i[0]+=1
            print (i)
            mid=(l+r)//2
            

            while l!=r:
                
                #check left side
                
                if nums[mid]==nums[mid-1]:
                    lenleft=len(nums[l:mid-1])
                    lenright=len(nums[mid+1:r+1])
                    
                    if lenleft%2==0:
                        l=mid+1
                        return search(l,r)
                    else:
                        r=mid-2
                        return search(l,r)
                #check left right
                elif nums[mid]==nums[mid+1]:
                    lenleft=len(nums[l:mid])
                    lenright=len(nums[mid+1:r+1])
                    if lenleft%2==0:
                        l=mid+2
                        return search(l,r)
                    else:
                        r=mid-1
                        return search(l,r)
            return nums[mid]
        
        
        return (search(0,len(nums)-1))
