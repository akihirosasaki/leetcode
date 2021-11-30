# @before-stub-for-debug-begin
from python3problem394 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        curNum=0
        curString=''
        for c in s:
            print(c,stack)
            if c=='[':
                stack.append(curString)
                stack.append(curNum)
                curString=''
                curNum=0
            elif c==']':
                num=stack.pop()
                prevString=stack.pop()
                curString=prevString+num*curString
            elif c.isdigit():
                curNum=curNum*10+int(c)
            else:
                curString+=c
        return curString
# @lc code=end

