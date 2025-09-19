# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        t=[]
        if root.left is not None:   # root[1]
            lp=self.inorderTraversal(root.left)
            for i in lp:
                t.append(i)
        t.append(root.val)
        if root.right is not None:
            rp=self.inorderTraversal(root.right)
            for i in rp:
                t.append(i)
        return t