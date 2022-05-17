class queueNode:
    def __init__(self, val: int):
        self.val=val
        self.next=None

class MyCircularQueue:

    def __init__(self, k: int):
        self.size=k
        self.cur=0
        
        self.head=None
        self.rear=None

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            if self.head is None:
                self.head=queueNode(value)
                self.rear=self.head
            else:
                self.rear.next=queueNode(value)
                self.rear=self.rear.next
            
            self.cur+=1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.cur==1:
            self.head=None
            self.rear=None
            self.cur=0
            return True
        if not self.isEmpty():
            self.rear.next=self.head.next
            self.head=self.head.next
        
            self.cur-=1
            return True
        else:
            return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.head.val
        else:
            return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.rear.val
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.head is None

    def isFull(self) -> bool:
        return self.cur==self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
