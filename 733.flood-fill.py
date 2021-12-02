#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        visited=[ [False]*len(image[0]) for i in range(len(image))]
        rl=len(image)
        cl=len(image[0])
        self.output=copy.deepcopy(image)
        self.dfs(image,sr,sc,rl,cl,newColor,image[sr][sc], visited)
        return self.output
        

    def dfs(self, image: List[List[int]], sr: int, sc: int, rl: int, cl: int, newColor: int, baseColor: int, visited: List[List[bool]]):
        if (sc<0 or sc>=cl or sr<0 or sr>=rl):
            return 
        if image[sr][sc]!=baseColor or visited[sr][sc]:
            return 

        visited[sr][sc]=True
        
        self.output[sr][sc]=newColor
        self.dfs(image, sr+1, sc, rl, cl, newColor, baseColor, visited)
        self.dfs(image, sr-1, sc, rl, cl, newColor, baseColor, visited)
        self.dfs(image, sr, sc+1, rl, cl, newColor, baseColor, visited)
        self.dfs(image, sr, sc-1, rl, cl, newColor, baseColor, visited)
    
        

# @lc code=end

