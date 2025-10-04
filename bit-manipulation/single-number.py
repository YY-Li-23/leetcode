class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            t=0
            for j in range(len(nums)):
                if nums[i]==nums[j]:
                    t+=1
            if t==1:
                return nums[i]
        