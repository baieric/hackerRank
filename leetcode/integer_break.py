# https://leetcode.com/problems/integer-break/

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 2
        best = 0

        while s <= n:
            d = n//s
            r = n%s

            if r > 0:
                new = (d ** (s-r)) * ((d + 1) ** r)
            else:
                new = d ** s

            best = max(best, new)
            s+= 1

        return best
