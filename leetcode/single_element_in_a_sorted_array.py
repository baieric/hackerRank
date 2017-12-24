# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def search (start, end):
            if end <= start:
                return nums[start]
            if start >= end:
                return nums[end]
            mid = ((end + start) / 2)
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] != nums[mid+1]:
                return search(start, mid - 1)
            else:
                return search(mid+2, end)
        return search(0, len(nums) - 1)
