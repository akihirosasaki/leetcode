#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#

# @lc code=start
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = [ ]
        dd = collections.defaultdict(list)
        if not mat: return result
        for i in range(0, len(mat)):
            for j in range(0, len(mat[0])):
                dd[i+j+1].append(mat[i][j])
        for k in sorted(dd.keys()):
            if k%2==1: dd[k].reverse()
            result += dd[k]
        return result
        
        

# @lc code=end

