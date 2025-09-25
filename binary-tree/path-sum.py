# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False  #path
        def sum_(node,s):
            if node.left is None and node.right is None:
                return s==targetSum
            res =False
            if node.left:
                s_left=s+node.left.val
                res=res or sum_(node.left, s_left) # add up
            if node.right:
                s_right=s+node.right.val
                res=res or sum_(node.right,s_right)
            return res
        return sum_(root,root.val)
            

