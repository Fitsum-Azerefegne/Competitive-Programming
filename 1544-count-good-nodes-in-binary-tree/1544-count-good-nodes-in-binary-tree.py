# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0 

        goods = 0
        queue = deque([(root, root.val)])
        while queue:
            node, curr_max = queue.popleft()
            if node.val >= curr_max:
                goods += 1
            if node.left:
                queue.append((node.left, max(node.val, curr_max)))
            if node.right:
                queue.append((node.right, max(node.val, curr_max)))

        return goods