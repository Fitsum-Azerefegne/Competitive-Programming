# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        result = []  
        queue = deque([(root, 0)])  
        while queue:
            node, level = queue.popleft()  
            if level == len(result):
                result.append([])  
            result[level].append(node.val)  
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        averages = [sum(level_values) / len(level_values) for level_values in result]
        return averages