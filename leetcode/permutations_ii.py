# https://leetcode.com/problems/permutations-ii/#/description

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        s = []
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [[nums[0]]]
        seen = set()
        for i in range(len(nums)):
            if nums[i] not in seen:
                p = self.permuteUnique(nums[0:i] + nums[i+1:])
                for j in p:
                    s.append([nums[i]] + j)
                seen.add(nums[i])
        return list(s)
