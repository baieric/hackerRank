# https://leetcode.com/problems/spiral-matrix-ii/#/description

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        a = [[0 for x in range(n)] for y in range(n)]
        layer = 0
        num = 1
        while layer <= n//2:
            for i in range(layer, n - layer):
                a[layer][i] = num
                num += 1
            for i in range(layer+1, n - layer):
                a[i][n-layer-1] = num
                num += 1
            for i in range(n-layer-2, layer - 1, -1):
                a[n-layer-1][i] = num
                num += 1
            for i in range(n-layer-2, layer, -1):
                a[i][layer] = num
                num += 1
            layer += 1
        return a
