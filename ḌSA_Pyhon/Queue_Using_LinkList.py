class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            data = self.front.data
            if self.front == self.rear:
                self.front = None
                self.rear = None
            else:
                self.front = self.front.next
            return data

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            return self.front.data

    def display(self):
        current = self.front
        if self.is_empty():
            print("Queue is empty")
            return
        else:
            print("Queue elements are:")
            while current:
                print(current.data, end=" ")
                current = current.next
            print()

# Example usage:
if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    q.display()  # Output: 10 20 30

    print("Peek:", q.peek())  # Output: Peek: 10

    print("Dequeue:", q.dequeue())  # Output: Dequeue: 10
    q.display()  # Output: 20 30

    print("Dequeue:", q.dequeue())  # Output: Dequeue: 20
    q.display()  # Output: 30

    print("Dequeue:", q.dequeue())  # Output: Dequeue: 30
    q.display()  # Output: Queue is empty
