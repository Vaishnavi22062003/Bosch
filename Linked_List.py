class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next
 
class Linked_List:
    def __init__(self):
        self.head=None
    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node
    def insert_at_end(self,data):
        node=Node(data,None) 
        if self.head == None:
            self.head=node
            return 
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=node
 
    def delete_at_specific_position(self,position):
        if self.head is None:
            raise Exception("Cannot delete from an empty list.")
        if position < 0 or position >= self.get_length():
            raise Exception("Invalid index")
        if position==0:
            self.head=self.head.next
            return
        else:
            temp = self.head
            count = 0
            temp=self.head
            index=0
            while(temp):
                if index==position-1:
                    temp.next=temp.next.next
                temp=temp.next
                index+=1
           
 
    def delete_by_value(self,element):
        if self.head is None:
            return
        if self.head.data==element:
            self.head=self.head.next
            return     
        temp=self.head
        while temp.next:
            if temp.next.data==element:
                temp.next=temp.next.temp
                break
            temp=temp.next   
    def get_length(self):
        count=0
        temp=self.head
        while temp:
            temp=temp.next
            count+=1
        return count
    def display(self):
        if self.head == None:
            print("Linked List is empty")
            return 
        temp=self.head
        llst=[]
        while(temp):
            llst.append(str(temp.data)) 
            temp = temp.next
        output = " -> ".join(llst)
        print(output)

if __name__ == '__main__':
    l1=Linked_List()
    l1.insert_at_begining(10)
    l1.insert_at_begining(22)
    l1.insert_at_end(78)
    l1.insert_at_end(50)
    l1.insert_at_end(60)
    l1.insert_at_end(70)
    l1.insert_at_begining(6)
    l1.insert_at_begining(9)
 
    l1.display()
    l1.delete_at_specific_position(2)
    print("\nAfter removing at specific position at 2 ")
    l1.display()
    l1.delete_by_value(9)
    print("\nAfter removing specific value 9 ")
    l1.display()
    print("\nLength of the Linked List ",l1.get_length())