#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        dict={
            "(":")",
            "{":"}",
            "[":"]"
            }
        stack=[]
        for bracket in s:
            if bracket in dict.keys():
                stack.append(bracket)
            else:
                if not stack:
                    return False
                else:
                    open=stack.pop()
                    if dict[open]!=bracket:
                        return False
        return not stack

            

# @lc code=end

