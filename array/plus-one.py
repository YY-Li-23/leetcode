class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        k=len(digits)
        n=0
        for i in range(len(digits)):
            n+=digits[i]*(10**(k-i-1))

        n+=1

        return[int(d) for d in str(n)]   #loop over a str
        