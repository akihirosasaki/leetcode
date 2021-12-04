#
# @lc app=leetcode id=941 lang=python3
#
# [941] Valid Mountain Array
#

# @lc code=start
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        i,tmp=0,[0]*(len(arr)-1)
        while i<len(arr)-1:
            if arr[i]<arr[i+1]:
                tmp[i]=1
            elif arr[i]>arr[i+1]:
                tmp[i]=-1
            else:
                tmp[i]=0
            i+=1
        if 0 in tmp:
            return False
        
        j,cnt1,cnt2=0,0,0
        while j<len(tmp)-1:
            if tmp[j]==1 and tmp[j+1]==-1:
                cnt1+=1
                cnt2+=1
            if tmp[j]==-1 and tmp[j+1]==1:
                cnt2+=1
            j+=1
        if cnt1==1 and cnt2==1:
            return True
        else:
            return False
# @lc code=end

