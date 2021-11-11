#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output=0
        for i in range(0,len(s)):
            hashset=set()
            for j in range(i,len(s)):
                if s[j] in hashset:
                    break
                hashset.add(s[j])
            if output<len(hashset):
                output=len(hashset)
        return output
# @lc code=end

