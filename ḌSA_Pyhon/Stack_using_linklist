class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        else:
            popped_item = self.top.data
            self.top = self.top.next
            return popped_item

    def peek(self):
        if self.is_empty():
            print("Stack is empty. Cannot peek.")
            return None
        else:
            return self.top.data

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            current = self.top
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

# Example usage:
st = Stack()
st.push(1)
st.push(2)
st.push(3)
st.display()  

print("Popped item:", st.pop())  
print("Peeked item:", st.peek())  
sts.display()  
