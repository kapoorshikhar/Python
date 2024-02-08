class StackUsingQueue:
    def __init__(self):
        self.queue1 = []  
        self.queue2 = []  

    def push(self, item):
      
        self.queue1.append(item)

    def pop(self):
        if not self.queue1:
            return "Stack is empty"
        
     
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))

        # Pop and return the last element from queue1
        popped_item = self.queue1.pop()

       
        self.queue1, self.queue2 = self.queue2, self.queue1

        return popped_item

    def top(self):
        if not self.queue1:
            return "Stack is empty"
        
        
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))

       
        top_item = self.queue1[0]

      
        self.queue2.append(self.queue1.pop())

      
        self.queue1, self.queue2 = self.queue2, self.queue1

        return top_item

    def is_empty(self):
        return len(self.queue1) == 0



stack = StackUsingQueue()
stack.push(1)
stack.push(2)
stack.push(3)

print("Top of the stack:", stack.top())  
print("Pop:", stack.pop())
print("Top of the stack:", stack.top()) 
print("Pop:", stack.pop())               
print("Is stack empty?", stack.is_empty()) 
print("Pop:", stack.pop())               
print("Is stack empty?", stack.is_empty()) 
