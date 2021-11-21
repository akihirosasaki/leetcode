#
# @lc app=leetcode id=622 lang=python3
#
# [622] Design Circular Queue
#

# @lc code=start
class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.max_size = k
        self.t = [0]*k
        self.front = self.rear = -1
        
    def enQueue(self, value: int) -> bool:
        if self.isEmpty()==True:
            self.t[0]=value
            self.size+=1
            self.front=self.rear=0
            return True
        
        if self.isFull()==False:
            if self.rear+1<self.max_size:
                self.t[self.rear+1]=value
                self.rear+=1
            else:
                self.t[0]=value
                self.rear=0
            self.size+=1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.isEmpty()==True:
            return False
        else:
            if self.front+1<self.max_size:
                self.t[self.front]=0
                self.front+=1
            else:
                self.t[self.front]=0
                self.front=0
            self.size-=1
            return True

    def Front(self) -> int:
        if self.isEmpty()==True:
            return -1
        else:
            return self.t[self.front]

    def Rear(self) -> int:
        if self.isEmpty()==True:
            return -1
        else:
            return self.t[self.rear]

    def isEmpty(self) -> bool:
        if self.size==0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.size>=self.max_size:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end

