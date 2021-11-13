#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]!=9:
            digits[-1]+=1
        else:
            length = len(digits)
            if min(digits)==9:
                digits = [0]*length
                digits.insert(0,1)
            else:
                for i in reversed(range(0,length)):
                    if digits[i]==9:
                        digits[i]=0
                    else:
                        digits[i]+=1
                        break

        return digits
# @lc code=end

