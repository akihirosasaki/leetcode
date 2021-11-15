#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output=[]
        for i in range(numRows):
            res=self.getRow(i)
            output.append(res)
        return output

    def getRow(self, rowIndex: int) -> List[int]:
        row=[1]*(rowIndex+1)
        for i in range(2, rowIndex+1):
            for j in range(1,i):
                row[i-j]+=row[i-j-1]
        return row

# @lc code=end

