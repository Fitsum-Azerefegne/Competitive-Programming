# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(node:Optional[TreeNode], curr_sum:int):
            if node == None:
                return False
            if node.left == None and node.right == None :
                curr_sum += node.val
                if curr_sum == targetSum:
                    return True
                else:
                    return False
            curr_sum += node.val

            return dfs(node.left,curr_sum) or dfs(node.right,curr_sum)
        return dfs(root, 0)