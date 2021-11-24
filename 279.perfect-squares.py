#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        list=[]
        i=1
        while i*i<=n:
            list.append(i*i)
            i+=1
        
        cnt=0
        toCheck={n}
        while toCheck:
            cnt+=1
            temp=set()
            for x in toCheck:
                for y in list:
                    if x==y:
                        return cnt
                    if x<y:
                        break
                    temp.add(x-y)
            toCheck=temp
        return cnt

    
# @lc code=end

