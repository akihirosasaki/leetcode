#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators=["+","-","*","/"]
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                num1=int(stack.pop())
                num2=int(stack.pop())
                if token=="+":
                    num=num2+num1
                if token=="-":
                    num=num2-num1
                if token=="*":
                    num=num2*num1
                if token=="/":
                    num=num2/num1
                stack.append(num)
        return int(stack[0])
# @lc code=end

