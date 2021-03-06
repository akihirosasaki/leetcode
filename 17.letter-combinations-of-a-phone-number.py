#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
"""my answer"""
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
#                    '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
#         length=len(digits)
#         if length==0:
#             return []
#         dict={}
#         cnt=0
#         for digit in digits:
#             for word in mapping[digit]:
#                 dict.setdefault(cnt, []).append(word)
#             cnt+=1
        
class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if '' == digits: return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        ret=['']
        for c in digits:
            tmp=[]
            for y in ret:
                for x in kvmaps[c]:
                    tmp.append(y+x)
                    print(tmp)
            ret=tmp
        
        return ret


# @lc code=end

