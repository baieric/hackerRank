# https://leetcode.com/problems/combination-sum-iii/

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        arr = []

        def recurse(comb, arr, start, k, n):
            if len(comb) == k and n == 0:
                arr.append(comb)
                return
            for i in range(start, 10):
                recurse(comb + [i], arr, i+1, k, n-i)
            return

        recurse([], arr, 1, k, n)

        return arr
