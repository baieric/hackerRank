# https://leetcode.com/problems/next-greater-element-ii

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        ret = [-1 for x in nums]
        n = len(nums)

        for i in range(n * 2):
            num = nums[i % n]
            while len(stack) != 0 and nums[stack[-1]] < num:
                ret[stack[-1]] = num
                stack.pop()
            if i < n:
                stack.append(i)
        return ret
