class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        if numRows>=3:
            res=[[1],[1,1]]
            for i in range(2,numRows): #from row 3
                pre=res[-1]   # last row
                row=[1]  # starts with 1

                for j in range(1,len(pre)):
                    row.append(pre[j-1]+pre[j])
                row.append(1) # it ends with 1 too
                res.append(row)

            return res



        