#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rl=len(mat)
        cl=len(mat[0])
        visited=[ [False]*cl for i in range(rl)]
        output=copy.deepcopy(mat)
        for i in range(rl):
            for j in range(cl):
                count=0
                tmpVisited=copy.deepcopy(visited)
                output[i][j]=self.dfs(mat,i,j,rl,cl,count,tmpVisited)
        return output

    def dfs(self, mat, sr, sc, rl, cl, count,visited):
        # print(sr,sc,visited,count)
        if (sr<0 or sr>=rl or sc<0 or sc>=cl or visited[sr][sc]):
            return
        if mat[sr][sc]==0:
            return count
        visited[sr][sc]=True
        count+=1
        n1=self.dfs(mat, sr+1, sc, rl, cl, count, visited)
        n2=self.dfs(mat, sr, sc+1, rl, cl, count, visited)
        n3=self.dfs(mat, sr-1, sc, rl, cl, count, visited)
        n4=self.dfs(mat, sr, sc-1, rl, cl, count, visited)
        return min(n1,n2,n3,n4)
        
# @lc code=end

