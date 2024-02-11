class QueueUsingStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, item):
        self.stack_in.append(item)

    def dequeue(self):
        if not self.stack_out:
            if not self.stack_in:
                return None
            # Transfer elements from stack_in to stack_out
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        # Pop from stack_out
        return self.stack_out.pop()

    def is_empty(self):
        return not (self.stack_in or self.stack_out)

    def size(self):
        return len(self.stack_in) + len(self.stack_out)

# Example usage:
if __name__ == "__main__":
    q = QueueUsingStacks()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print("Dequeue:", q.dequeue())  # Should dequeue 1
    print("Dequeue:", q.dequeue())  # Should dequeue 2
    q.enqueue(4)
    print("Dequeue:", q.dequeue())  # Should dequeue 3
    print("Dequeue:", q.dequeue())  # Should dequeue 4
    print("Dequeue:", q.dequeue())  # Should dequeue None since the queue is empty
