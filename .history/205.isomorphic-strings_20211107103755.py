#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        for i in range(len(s)):
            print(s[i],t[i])
            if s[i] not in d.keys():
                if t[i] in d.values():
                    return False
                d[s[i]]=t[i]
            else:
                if d[s[i]]!=t[i]:
                    return False
            print(d)
        return True
# @lc code=end

