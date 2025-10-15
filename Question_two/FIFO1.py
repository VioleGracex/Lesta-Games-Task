class FIFOQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, item):
        self.stack_in.append(item)
        print("Queue", item)

    def dequeue(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:
            print("Queue size 0")
            return None
        item = self.stack_out.pop()
        print("Dequeue", item)
        return item

    def is_empty(self):
        return not (self.stack_in or self.stack_out)

    def size(self):
        return len(self.stack_in) + len(self.stack_out)

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