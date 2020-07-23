class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.length:
            return -1
        if index == 0: 
            return self.head.val
        elif index == self.length:
            return self.tail.val
        else:
            current = self.head 
            count = 0 # counter for iteration
            while current is not None:
                if count == index:
                    return current.val
                current = current.next
                count += 1
            return -1 # if list is empty

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
            self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
            
        elif index == (self.length):
            self.addAtTail(val)
        else:
            count = 0
            prev = None
            current = self.head
            newNode = Node(val)
            while count != index and current.next != None:
                prev = current
                current = current.next
                count += 1
            if count == index:
                prev.next = newNode
                newNode.next = current
                self.length += 1
        
        
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            self.head = self.head.next
            self.length -= 1 
        else:
            current = self.head 
            count = 0
            prev = None 
            while count != index and current.next != None:
                prev = current
                current = current.next
                count += 1
            if count == index: 
                prev.next = current.next 
                self.length -= 1 