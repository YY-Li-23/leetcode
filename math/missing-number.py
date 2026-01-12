class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        full=[]
        res=[]
        for i in range(0,len(nums)+1):
            full.append(i)
            i+=1
    
        
        for j in full:
            if j not in nums:
                return j
        
        

            