#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        length=len(digits)
        if length==0:
            return []
        dict={}
        cnt=0
        for digit in digits:
            for word in mapping[digit]:
                dict.setdefault(cnt, []).append(word)
            cnt+=1
        
        tmpStr=""
        for i in dict.keys:
            print(i)




# @lc code=end

