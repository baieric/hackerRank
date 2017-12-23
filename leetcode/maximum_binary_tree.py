# https://leetcode.com/problems/maximum-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        stack = []
        for i in range(len(nums)):
            cur = TreeNode(nums[i])
            while (len(stack) and stack[-1].val < nums[i]):
                cur.left = stack.pop()
            if len(stack):
                stack[-1].right = cur
            stack.append(cur)
        return stack[0]
