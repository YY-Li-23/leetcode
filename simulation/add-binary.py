class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i=len(a)-1
        j=len(b)-1           #starts with the right side
        k=0
        result=""
        while i>=0 or j>=0 or k>0:   
            if i>=0:
                digit_a=int(a[i])
            else:
                digit_a=0
            if j>=0:
                digit_b=int(b[j])
            else:
                digit_b=0
            total=digit_a + digit_b+k
            bit=total%2    
            k=total//2
            result=str(bit)+result    # str!

            i-=1
            j-=1
        return result

        