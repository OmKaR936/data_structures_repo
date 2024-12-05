class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def print_list(self):
        temp=self.head
        while temp != None:
            print(temp.value)
            temp=temp.next
    
    def append_at_end(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
    
    def pop_from_end(self):
        if self.length==0:
            return None
        elif self.length==1:
            self.head=None
            self.tail=None
            self.length==0
        else:
            temp=self.head
            while(temp.next!=None):
                pre=temp
                temp=temp.next
            self.tail=pre
            self.tail.next=None
            self.length-=1
    def add_at_beginning(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
    
    def pop_first(self):
        if self.length==0:
            return None
        temp=self.head
        self.head=temp.next
        temp.next=None
        self.length-=1
        if self.length==0:
            self.tail=None
        # return temp

my_linked_list=LinkedList(1)
my_linked_list.append_at_end(2)
my_linked_list.append_at_end(3)
my_linked_list.pop_first()
my_linked_list.print_list()