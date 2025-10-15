import time
from collections import deque

class FIFOStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, item):
        self.stack_in.append(item)

    def dequeue(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:
            return None
        item = self.stack_out.pop()
        return item

    def is_empty(self):
        return not (self.stack_in or self.stack_out)

    def size(self):
        return len(self.stack_in) + len(self.stack_out)

class FIFODeque:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.queue:
            return None
        item = self.queue.popleft()
        return item

    def is_empty(self):
        return not self.queue

    def size(self):
        return len(self.queue)

def test_fifo(qclass, n):
    q = qclass()
    start = time.time()
    for i in range(n):
        q.enqueue(i)
    for i in range(n):
        q.dequeue()
    end = time.time()
    return end - start

def main():
    n = 100000
    
    t1 = test_fifo(FIFODeque, n)
    t2 = test_fifo(FIFOStacks, n)
    print(f"FIFODeque {t1:.6f} секунд")
    print(f"FIFOStacks {t2:.6f} секунд")

if __name__ == "__main__":
    main()