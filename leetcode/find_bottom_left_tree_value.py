# https://leetcode.com/problems/find-bottom-left-tree-value

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        node = None
        while len(queue) > 0:
            node = queue.pop(0)
            if node.right is not None:
                queue.append(node.right)
            if node.left is not None:
                queue.append(node.left)
        return node.val
