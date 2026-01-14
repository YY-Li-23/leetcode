class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(n+1):
         
            s = bin(i)[2:].zfill(8)
            res.append(s.count("1"))

        return res