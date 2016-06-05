# Solution to https://leetcode.com/problems/search-a-2d-matrix-ii/
class Solution(object):
    def search(self, matrix, target, top, bottom, left, right):
        print(str(top) + " " + str(bottom) + " " + str(left) + " " + str(right))
        if bottom < top or right < left:
            return False
        if bottom - top <= 1 and right - left <= 1:
            return matrix[top][left] == target or matrix[top][right] == target or matrix[bottom][left] == target or matrix[bottom][right] == target
        midx = left + (right - left)/2
        midy = top + (bottom-top)/2

        mid = matrix[midy][midx]
        print(mid)
        if mid == target:
            return True
        if mid > target:
            yOOB = midy - 1 < 0
            xOOB = midx - 1 < 0
            if not yOOB and not xOOB:
                return self.search(matrix, target, top, bottom, left, midx-1) or self.search(matrix, target, top, midy-1, midx, right)
            if yOOB:
                return self.search(matrix, target, top, bottom, left, midx-1)
            if xOOB:
                return self.search(matrix, target, top, midy-1, midx, right)
            return False
        else:
            yOOB = midy + 1 >= len(matrix)
            xOOB = midx + 1 >= len(matrix[0])
            if not yOOB and not xOOB:
                return self.search(matrix, target, midy + 1, bottom, left, midx) or self.search(matrix, target, top, bottom, midx+1, right)
            if yOOB:
                return self.search(matrix, target, top, bottom, midx+1, right)
            if xOOB:
                return self.search(matrix, target, midy + 1, bottom, left, midx)
            return False

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        return self.search(matrix, target, top, bottom, left, right)
