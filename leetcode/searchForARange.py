# Solution to https://leetcode.com/problems/search-for-a-range/
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums) - 1
        left = None
        while start <= end :
            mid = start + (end - start)/2
            print(mid)
            if nums[mid] >= target:
                if nums[mid] == target and mid == 0:
                    left = -1
                    break
                end = mid - 1
            else:
                if mid + 1 < len(nums) and nums[mid+1] == target:
                    left = mid
                    break
                start = mid + 1

        if left == None:
            return [-1, -1]

        start = 0
        end = len(nums) - 1
        right = None
        while start <= end :
            mid = start + (end - start)/2
            if nums[mid] <= target:
                if nums[mid] == target and mid == len(nums)-1:
                    right = mid + 1
                    break
                start = mid + 1
            else:
                if mid - 1 < len(nums) and nums[mid-1] == target:
                    right = mid
                    break
                end = mid - 1

        return [left+1, right-1]
