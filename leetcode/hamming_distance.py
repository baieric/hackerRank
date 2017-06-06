# https://leetcode.com/problems/hamming-distance

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if x == 0 and y == 0:
            return 0

        a = x % 2
        b = y % 2

        if a != b:
            return 1 + self.hammingDistance(int(x/2), int(y/2))
        return self.hammingDistance(int(x/2), int(y/2))
