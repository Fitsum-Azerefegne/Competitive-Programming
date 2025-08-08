# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        summ = 0
        def dfs(node: Optional[TreeNode], is_left:bool):
            nonlocal summ
            if not node:
                return
            if not node.left and not node.right and is_left:
                summ += node.val
            dfs(node.left, True)
            dfs(node.right, False)
        dfs(root, False)
        return summ
            