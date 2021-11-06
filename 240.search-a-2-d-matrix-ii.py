#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return None
        print(matrix)
        m=len(matrix)
        n=len(matrix[0]) 
        
        # if (m,n)==(1,1):
        #     return matrix[0][0]==target
        if m==1:
            return target in matrix[0]
        if n==1:
            return target in sum(matrix, [])
        if m<=2 and n<=2:
            return target in sum(matrix, [])
         
        midM=m//2
        midN=n//2
        p=matrix[midM][midN]
        newMatrix=self.helper(matrix, target, p)
        
        if type(newMatrix)==int:
            return True

        return self.searchMatrix(newMatrix, target)
        
    def helper(self, matrix: List[List[int]], target: int, p: int):
        pIndex = self.find(p, matrix)
        newMatrix=[]
        if p > target:
            deleteMatrix = matrix[:pIndex[0]]
            for i in range(len(deleteMatrix)):
                newMatrix.append(deleteMatrix[i][:pIndex[1]])
        elif p < target:
            deleteMatrix = matrix[pIndex[0]:]
            for i in range(len(deleteMatrix)):
                newMatrix.append(deleteMatrix[i][pIndex[1]:])
        else:
            newMatrix=matrix[pIndex[0]][pIndex[1]]
        
        return newMatrix
        
        
    def find(self, element, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == element:
                    return (i, j)

        
# @lc code=end

