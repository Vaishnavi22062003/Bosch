class stack:
    def __init__(self):
        self.stack=[]

    def push(self,element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack)==0
    
    def size(self):
        return len(self.stack)

mystack=stack()

mystack.push('A')
mystack.push('B')
mystack.push('C')

print("Stack: ", mystack.stack)
print("Pop: ", mystack.pop())
print("Stack after Pop: ", mystack.stack)
print("Peek: ", mystack.peek())
print("isEmpty: ", mystack.isEmpty())
print("Size: ", mystack.size())