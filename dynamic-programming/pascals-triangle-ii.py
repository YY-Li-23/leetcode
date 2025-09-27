class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        res=[[1],[1,1]]
       
        for i in range(2,rowIndex+1): 
            pre=res[-1]   # last row
            row=[1]  # starts with 1
            for j in range(1, len(pre)):
                row.append(pre[j-1]+pre[j])
            row.append(1) # it ends with 1 too
            res.append(row)

        return res[-1]