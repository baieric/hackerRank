# https://leetcode.com/problems/counting-bits/
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        arr = [0]
        twos = 1
        for i in range(1, num + 1):
            if i == twos * 2:
                twos = twos * 2
            arr.append(1 + arr[i - twos])
        return arr
