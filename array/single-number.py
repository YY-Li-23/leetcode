class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result ^= n   # XOR: cancels out numbers that appear twice
        return result
        