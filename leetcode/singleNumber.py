# https://leetcode.com/problems/single-number/
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        found = set()
        for i in nums:
            if i in found:
                found.remove(i)
            else:
                found.add(i)

        for i in found:
            return i
