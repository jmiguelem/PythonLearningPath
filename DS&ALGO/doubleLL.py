class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev 

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count
    
    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr
    
    def print_forward(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '---->'
            itr = itr.next

        print(llstr)
    
    def print_backward(self):
        if self.head is None:
            print("Double Linked List is empty")
            return
        
        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += itr.data + '--->'
            itr = itr.prev
        print("Link list in reverse: ", llstr)

    def insert_at_begining(self, data):
        node = Node(data, self.head, None)
        self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None, itr)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("invalid index")

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        count  = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1


ll = DoubleLinkedList()
ll.insert_at_end(1)
ll.insert_at_end(4)
ll.insert_at_begining(5)
ll.insert_at_begining(89)
ll.insert_values(['hola','como','estas','?'])
ll.print_forward()
print(ll.get_length())
ll.remove_at(2)
ll.print_forward()
ll.insert_at(2, "vienes")
ll.print_forward()
ll.print_backward()