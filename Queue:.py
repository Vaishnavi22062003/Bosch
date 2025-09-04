class Queue:
    def __init__(self):
        self.queue=[]

    def enqueue(self,value):
        self.queue.append(value)

    def dequeue(self):
        if self.isempty():
            return "queue is empty"
        return self.queue.pop(0)
    
    def peek(self):
        if self.isempty():
            return "queue is empty"
        return self.queue[0]
    
    def isempty(self):
        return len(self.queue)==0
    
    def size(self):
        return len(self.queue)
    
myqueue= Queue()

myqueue.enqueue('A')
myqueue.enqueue('B')
myqueue.enqueue('C')
print("Dequeue:",myqueue.dequeue())
print("Peek: ",myqueue.peek())
print("Queue after dequeuing: ",myqueue.queue)
print("Isempty: ",myqueue.isempty())
print("Size: ",myqueue.size())