#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columnList = [list(x) for x in zip(*board)]
        subsquares = [[board[j][i] for j in range(x, x + 3) for i in range(y, y + 3)] for x in range(0, 9, 3) for y in range(0, 9, 3)]
        
        for row in board:
            if self.containsDuplicate(row)==True:
                return False
        for column in columnList:
            if self.containsDuplicate(column)==True:
                return False
        for square in subsquares:
            if self.containsDuplicate(square)==True:
                return False
        return True

    def containsDuplicate(self, nums: List[str]) -> bool:
        hashset = set() 
        for n in nums:
            if n==".":
                continue
            if (n in hashset):
                return True
            hashset.add(n)
        return False

# @lc code=end

