# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            left_h=height(node.left)
            right_h=height(node.right)
            return 1+max(left_h,right_h)
        if not root:
            return True
        left_height=height(root.left)
        right_height=height(root.right)

        if abs(left_height-right_height)>1:   # height balanced means left and right (abs)<2
            return False 
        return self.isBalanced(root.left) and self.isBalanced(root.right)