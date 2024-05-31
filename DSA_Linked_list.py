class Node:
    def __init__(self, data,next=None):
        self.data=data
        self.next = next
class LinkedList:
    def __init__(self,head=None):
        self.head = head
    
    def add(self,data):
        new = Node(data) #Create a Node
        if self.head:
            temp = self.head 
            while temp.next != None: 
                temp = temp.next
            temp.next = new
        else:
            self.head = new
    
    def print_linked_list(self,first=None):
        self.first = first
        first = self.head
        while first:
            print(first.data)
            first = first.next
    
    def insert(self,new=None):
        self.new = new
        newNode = Node(new)
        newNode.next = self.head
        self.head = newNode
    
    def insert_end(self,new=None):
        self.new = new
        new = Node(new)
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new
    
    def insert_after_a_given_node(self,data,x):
        self.data = data
        self.x = x
        temp = self.head
        newNode = Node(data)
        while temp:
            if temp.data == x:
                newNode.next = temp.next
                temp.next = newNode
            temp = temp.next
    
    def delete_node(self,value):
        temp = self.head
        while temp != None:
            if temp.data == value:
                break
            prev = temp
            temp = temp.next
        prev.next = temp.next

    def search_node(self,x):
        current = self.head
        while current != None:
            if current.data == x :
                print("Found")
            else:
                print("Not Found")
            current = current.next
    
    def sort(self):
        temp = self.head
        a = []
        while temp:
            a.append(temp.data)
            temp = temp.next
        a.sort()
        new = LinkedList()
        for i in a:
            new.add(i)
        new.print_linked_list()
    
obj = LinkedList()
obj.add(10)
obj.add(20)
obj.add(30)
obj.add(40)
obj.insert(70)
obj.insert_after_a_given_node(50,40)
obj.insert_end(90)
obj.delete_node(30)
obj.sort()
obj.print_linked_list()


#############################################################    CIRCULAR LINKED LIST    ######################################################

class C_Node:
    def __init__(self,data=None):
        self.data = data
        self.next = next
class Circluar_linked_list:
    def __init__(self,head=None):
        self.head = head
    
    def print_list(self, first=None):
        self.first = first
        first = self.head
        while first.next:
            print(first.data)
            if first.next == self.head:
                break
            first = first.next

cir_obj = Circluar_linked_list()
cir_obj.head = Node(5)
second = Node(10)
third = Node(15)

cir_obj.head.next = second
second.next = third
third.next = cir_obj.head
cir_obj.print_list()

#############################################################    DOUBLE LINKED LIST    ######################################################

class Double_node:
    def __init__(self,data=None, next=None, prev= None):
        self.data = data
        self.next = next
        self.prev = prev

class Doubl_linked_list:
    def __init__(self,head=None):
        self.head = head
    def print_list(self,first = None):
        self.first = first
        first = self.head
        while first:
            print(first.data)
            first = first.next

double_obj = Doubl_linked_list()
double_obj.head = Node(15)
second = Node(25)
third = Node(35)

double_obj.head.prev = None
second.prev = double_obj.head
third.pre = second
double_obj.print_list()


#############################################################   LINKED LIST    ######################################################

class Node:
    def __init__(self,data=None, next=None):
        self.data = data
        self.next = next
class LinkedList2:
    def __init__(self):
        self.head = None
    
    def insert_at_the_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def print_my_ll(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        ll_str = ""
        
        while itr:
            ll_str += str(itr.data) + "-->"
            itr = itr.next
            
        print(ll_str)
        
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data,None)
            
    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            
    def get_lenth_ll(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count
    
    def remove_at(self,index):
        if index<0 or index>=self.get_lenth_ll():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            
            itr = itr.next
            count +=1
            
    def insert_at(self,index,data):
        if index<0 or index>=self.get_lenth_ll():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_the_beginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data,itr.next)
                break
        
        itr = itr.next
        count +=1


if __name__ == "__main__":
    ll = LinkedList2()
    ll.insert_values(["Banana","Mangoes","Grapes","Orange"])
    #ll.insert_at_the_beginning(5)
    #ll.insert_at_the_beginning(77)
    #ll.insert_at_end(89)
    ll.print_my_ll()
    ll.insert_at(0,"Batman")
    #ll.remove_at(2)
    print("Lenght : ",ll.get_lenth_ll())
    ll.print_my_ll()