import heapq
class MinStack(object):
    heap = []
    stack = []
    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        heapq.heappush(self.heap, val)
        self.stack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        element = self.stack.pop()
        for i, v in enumerate(self.heap):
            if element == v:
                self.heap[i] = self.heap[-1]
                self.heap.pop()
                heapq.heapify(self.heap)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.heap[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
