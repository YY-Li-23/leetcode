# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid=len(nums)//2
        root=TreeNode(nums[mid]) # find the root
        left_part=nums[:mid]
        root.left=self.sortedArrayToBST(left_part) #here we go again
        right_part=nums[mid+1:]   #+1!
        root.right=self.sortedArrayToBST(right_part)
        return root 

        
