class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 !=0:
            return False
        stack=[]
        mapping = {')': '(', ']': '[', '}': '{'}   #all right keys
        for i in s:
            if i in mapping:
                if not stack or stack[-1]!=mapping[i]:  
                #when there is a right key but there is no left in the stack (not stack) => false, stack[-1] the first one in the stack doesn' match =>"(]"
                    return False
                stack.pop()
            else:
                stack.append(i)

        return not stack
        