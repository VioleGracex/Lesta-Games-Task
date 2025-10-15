from collections import deque

class FIFOQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)
        print("Queue", item)

    def dequeue(self):
        if not self.queue:
            print("Queue size is 0")
            return None
        item = self.queue.popleft()
        print("Dequeue", item)
        return item

    def is_empty(self):
        return not self.queue

    def size(self):
        return len(self.queue)
    
def main():
    q = FIFOQueue()
    q.enqueue(3)
    q.dequeue()
    q.dequeue()
    q.enqueue(4)
    q.dequeue()
    q.dequeue()  

if __name__ == "__main__":
    main()    