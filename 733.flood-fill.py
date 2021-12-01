#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        visited=[ [False]*len(image) for i in range(len(image[0]))]
        rl=len(image)
        cl=len(image[0])
        self.dfs(image,sr,sc,rl,cl,newColor,image[sr][sc], visited)
        return image

    def dfs(self, image: List[List[int]], sr: int, sc: int, rl: int, cl: int, newColor: int, baseColor: int, visited: List[List[bool]]):
        if (sc<0 or sc>=cl or sr<0 or sr>=rl or image[sc][sr]!=baseColor or visited[sr][sc]):
            return 

        visited[sr][sc]=True
        
        image[sr][sc]=newColor
        self.dfs(image, sr+1, sc, rl, cl, newColor, baseColor, visited)
        self.dfs(image, sr-1, sc, rl, cl, newColor, baseColor, visited)
        self.dfs(image, sr, sc+1, rl, cl, newColor, baseColor, visited)
        self.dfs(image, sr, sc-1, rl, cl, newColor, baseColor, visited)
        
        

# @lc code=end

