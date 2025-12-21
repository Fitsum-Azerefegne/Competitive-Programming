class ListNode:
    def __init__(self, val, next=None):
        self.val = val    
        self.next = next  
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val
            
    def addAtHead(self, val: int) -> None:
        
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        if self.size == 0:  #if there was no node to begin with
            self.tail = new_node        
        self.size += 1
     

    def addAtTail(self, val: int) -> None:
        
        new_node = ListNode(val)  
        if not self.head:  
            self.head = new_node 
            self.tail = new_node  
        else:
            self.tail.next = new_node  
            self.tail = new_node  
    
        self.size += 1 

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 :
            index = 0
        if index > self.size:
            return None
        new_node = ListNode(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            if self.size == 0:
                self.tail = new_node
        else:
            curr = self.head
            for _ in range(index-1):
                curr = curr.next # we get the node before the given index
            new_node.next = curr.next
            curr.next = new_node
            if new_node.next is None:
                self.tail = new_node  # if the index is at the tail
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
        else:
            curr = self.head
            for _ in range(index-1):
                curr = curr.next
            curr.next = curr.next.next
            if curr.next is None:
                self.tail = curr
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)