class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <=0:
            return False
        while n %2 ==0:
            n//=2
        return n==1





    #    i=0
    #    while i <n:
    #       if 2**i==n:
    #           return True
    #       else:
    #           i+=1
    #   return False 