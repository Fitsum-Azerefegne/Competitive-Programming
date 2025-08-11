# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.values = []

        def in_order(node):
            if node:
                in_order(node.left)
                self.values.append(node.val)
                in_order(node.right)
        in_order(root)
        min_diff = float("inf")
        for i in range(1, len(self.values)):
            min_diff = min (min_diff, self.values[i] - self.values[i-1])
        return min_diff

        