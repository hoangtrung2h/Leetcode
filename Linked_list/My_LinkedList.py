class Node :
    def __init__(self,data):
        self.data = data
        self.next = None
class Linked_list:
    def __init__(self):
        self.head = None
    # add to tail
    def append(self,val):
        
        if self.head == None:
            self.head = Node
            return
        cur_node = self.head
        while cur_node.next != None :
            cur_node = cur_node.next
        cur_node.next = Node
    # display linked list
    def print_linked_list(self):
        if self.head == None:
            print("list is empty")
            return
        cur_node = self.head
        while cur_node!= None:
            if(cur_node.next == None):
                print(cur_node.data)
            else:
                print(cur_node.data,"-> ",end="")
            cur_node=cur_node.next
    # add at head 
    def add_at_head(self,Node):
        if self.head == None :
            return self.append(Node)
        head = self.head
        self.head = Node
        Node.next = head
    # delete at head
    def delete_at_head(self):
        if self.head == None:
            return
        head_node = self.head
        self.head = head_node.next
    # delete at tail
    def delete_at_tail(self):
        if self.head == None:
            return
        if self.head.next == None:
            return self.delete_at_head()
        cur_node = self.head
        pre_node = None
        while cur_node.next != None:
            pre_node = cur_node
            cur_node = cur_node.next
        if pre_node == None:
            return
        pre_node.next = None
    #delete at index 
    def delete_at_index(self,index):
        if self.head == None:
            return 
        if index ==0:
            return self.delete_at_head()
        cur_node = self.head
        pre_node = None
        count = 0
        while True:
            pre_node = cur_node
            cur_node = cur_node.next
            count+=1
            if count == index :
                pre_node.next = cur_node.next
                break
     #add at index 
    def add_at_index(self,index,val):
        
        new_node = Node(val)#create new node
        if self.head == None or index == 0 :# if list is empty or index == 0 add to head
            return self.add_at_head(new_node)
        cur_node = self.head
        pre_node = None
        count =0
        while True:
            pre_node = cur_node
            cur_node = cur_node.next
            count+=1
            if count == index:
                break
        # make a new node 
        pre_node.next = new_node
        new_node.next = cur_node
def main():
    myList = Linked_list()
    while(True):
        print("1.Append to linked list ")
        print("2.Add at head")
        print("3.Add at index")
        print("4.Remove at index")
        print("5.Remove at head")
        print("6.Remove at tail")
        print("7.Display your linked list")
        print("8.Quit")
        choice = int(input("Input your choice: "))
        if choice == 1:
            val = int(input("input your value you want to add: "))
            new_Node = Node(val)
            myList.append(new_Node)
        elif choice == 2 :
            val = int(input("input your value you want to add: "))
            new_Node = Node(val)
            myList.add_at_head(new_Node)
        elif choice == 3 :
            val = int(input("input your value you want to add: "))
            index = int(input("input position you want: "))
            myList.add_at_index(index,val)
        elif choice == 4:
            index = int(input("input position you want: "))
            myList.delete_at_index(index)
        elif choice == 5:
            myList.delete_at_head()
        elif choice == 6:
            myList.delete_at_tail()
        elif choice == 7:
            myList.print_linked_list()
        elif choice == 8:
            quit()
        print("-------------------")
if __name__ == '__main__':
    main()
    