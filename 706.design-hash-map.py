# @before-stub-for-debug-begin
from python3problem706 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
#

# @lc code=start
# class MyHashMap:
#     def eval_hash(self, key):
#         return ((key*1031237) & (1<<20) - 1)>>5

#     def __init__(self):
#         self.arr = [[] for _ in range(1<<15)]

#     def put(self, key: int, value: int) -> None:
#         t=self.eval_hash(key)
#         # print("put", key, value, self.arr[t])
#         if not self.arr[t]:
#             self.arr[t].extend([key,value])
#         elif key!=self.arr[t][0]:
#             self.arr[t].extend([key,value])
#         else:
#             self.arr[t][1]=value
#         # print(self.arr[t])
        
#     def get(self, key: int) -> int:
#         t=self.eval_hash(key)
#         # print("get", key, self.arr[t])
#         if not self.arr[t]:
#             return -1
#         elif key!=self.arr[t][0]:
#             return -1
#         else:
#             return self.arr[t][1]

#     def remove(self, key: int) -> None:
#         t=self.eval_hash(key)
#         # print("remove", key, self.arr[t])
#         if not self.arr[t]:
#             return 
#         if key==self.arr[t][0]:
#             self.arr[t].clear()
        
class MyHashMap:
    def eval_hash(self, key):
        return ((key*1031237) & (1<<20) - 1)>>5

    def __init__(self):
        self.arr = [[] for _ in range(1<<15)]
        
    def put(self, key, value):
        t = self.eval_hash(key)
        for i,(k,v) in enumerate(self.arr[t]):
            if k == key:
                self.arr[t][i] = (k, value)
                return
        self.arr[t].append((key, value))

    def get(self, key):
        t = self.eval_hash(key)
        for i,(k,v) in enumerate(self.arr[t]):
            if k == key: return v
        return -1

    def remove(self, key: int):
        t = self.eval_hash(key)
        for i,(k,v) in enumerate(self.arr[t]):
            if k == key:
                self.arr[t].remove((k,v))

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

