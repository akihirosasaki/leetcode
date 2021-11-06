# @before-stub-for-debug-begin
from python3problem744 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if not letters:
            return None

        i=-1
        for letter in letters:
            i+=1
            if letter<target:
                return letters[i]

        return letters[0]
            
        
# @lc code=end

