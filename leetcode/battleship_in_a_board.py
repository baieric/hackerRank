# https://leetcode.com/problems/battleships-in-a-board/description/
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        ships = 0
        for x in range(len(board)):
            row = board[x]
            for y in range(len(row)):
                if board[x][y] == 'X':
                    if y-1 >= 0 and board[x][y-1] == 'X':
                        continue
                    if x-1 >= 0 and board[x-1][y] == 'X':
                        continue
                    else:
                        ships = ships + 1
        return ships
