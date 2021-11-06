#
# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
#

# @lc code=start
class MyHashMap:
    def eval_hash(self, key):
        return ((key*1031237) & (1<<20) - 1)>>5

    def __init__(self):
        self.arr = [[] for _ in range(1<<15)]

    def put(self, key: int, value: int) -> None:
        t=self.eval_hash(key)
        print(self.arr[t])
        if not self.arr[t]:
            self.arr[t].extend([key,value])
        elif key!=self.arr[t][0]:
            self.arr[t].extend([key,value])
        else:
            self.arr[t][1]=value
        
    def get(self, key: int) -> int:
        t=self.eval_hash(key)
        print(self.arr[t])
        if not self.arr[t]:
            return -1
        elif key!=self.arr[t][0]:
            return -1
        else:
            return self.arr[t][1]

    def remove(self, key: int) -> None:
        t=self.eval_hash(key)
        if key==self.arr[t][0]:
            del self.arr[t]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

