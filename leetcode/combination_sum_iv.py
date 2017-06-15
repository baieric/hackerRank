# https://leetcode.com/problems/combination-sum-iv/
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        arr = [0 for x in range(target+1)]
        arr[0] = 1
        for i in range(target+1):
            for n in nums:
                if n <= i:
                    arr[i] += arr[i-n]
        return arr[target]
