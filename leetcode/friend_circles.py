# https://leetcode.com/problems/friend-circles/

class Solution(object):
    def dfs(self, M, v, x):
        for y in range(len(M)):
            if M[x][y] == 1 and not v[y]:
                v[y] = 1
                self.dfs(M, v, y)

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        v = [False for i in range(len(M))]
        count = 0

        for x in range(len(M)):
            if not v[x]:
                self.dfs(M, v, x)
                count += 1
        return count
                    
