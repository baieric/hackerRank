# https://leetcode.com/problems/top-k-frequent-elements/
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        l = d.items()
        l.sort(key=lambda x: x[1])
        ret = []
        end = len(l) - 1
        for i in range(k):
            ret.append(l[end - i][0])

        return ret
