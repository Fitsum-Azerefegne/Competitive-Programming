# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    
        ans = []
        def dfs(node:Optional[TreeNode], curr_sum:int, temp:List[int]):
    
            if node == None:
                return 
            temp.append(node.val)
            curr_sum += node.val
            if node.left == None and node.right == None and curr_sum == targetSum : 
                ans.append(temp.copy())
            

            dfs(node.left,curr_sum, temp)
            dfs(node.right,curr_sum, temp)
            temp.pop()
        dfs(root, 0, [])
        return ans
        