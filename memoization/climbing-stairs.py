class Solution:
    def climbStairs(self, n: int) -> int:
        if n>1:
            t=2**(n-2)+1
        else:
            t=n
        return t