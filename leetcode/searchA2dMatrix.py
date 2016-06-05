# Solution to https://leetcode.com/problems/search-a-2d-matrix/
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        start = 0
        numRows = len(matrix)
        numCols = len(matrix[0])
        while start < numRows:
            first = matrix[start][0]
            if first == target:
                return True
            if first > target:
                return False
            last = matrix[start][numCols-1]
            if last == target:
                return True
            if last > target:
                startCol = 0
                endCol = numCols - 1
                while endCol >= startCol:
                    mid = startCol + (endCol - startCol)/2
                    if matrix[start][mid] == target:
                        return True
                    elif matrix[start][mid] > target:
                        endCol = mid - 1
                    else:
                        startCol = mid + 1
                return False
            start += 1
        return False
