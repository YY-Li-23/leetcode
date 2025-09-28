class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best=0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j]>prices[i]:
                    d=prices[j]-prices[i]
                    if d>best:
                        best=d
        return best
                
        