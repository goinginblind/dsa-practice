class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    def __repr__(self):
        next_val = self.next.val if self.next else None
        self_val = self.val
        return f'Node:val={self_val}, next={next_val}'


class MyLinkedList:
    def __init__(self):
        self.dummy_head = ListNode(0)
        self.head = None
        self.tail = None
        self.size = 0


    def _getPrevNode(self, index: int) -> ListNode:
        if index < 0 or index > self.size:
            return None
        current_node = self.dummy_head
        counter = -1
        while current_node and counter < index:
            if counter == index - 1:
                return current_node
            current_node = current_node.next
            counter += 1
        return None
    
    
    def get(self, index: int) -> int:
        node_before_index = self._getPrevNode(index)
        if node_before_index and node_before_index.next:
            return node_before_index.next.val
        else:
            return -1


    def addAtHead(self, val: int) -> None:
        new_head = ListNode(val)
        if self.head:
            new_head.next = self.head
        else:
            self.tail = new_head
        self.dummy_head.next = new_head
        self.head = new_head
        self.size += 1


    def addAtTail(self, val: int) -> None:
        new_tail = ListNode(val)
        if self.tail:
            self.tail.next = new_tail
        else:
            self.dummy_head.next = new_tail
            self.head = new_tail
        self.tail = new_tail
        self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.size:
            self.addAtTail(val)
            return
        elif index == 0:
            self.addAtHead(val)
            return
        
        node_before_index = self._getPrevNode(index)
        if node_before_index:
            new_node = ListNode(val)
            new_node.next = node_before_index.next
            node_before_index.next = new_node
            self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        if index == 0:
            self.dummy_head.next = self.head.next
            self.head = self.head.next
            self.size -= 1    

        else:
            node_before_index = self._getPrevNode(index)
            if node_before_index:
                if index == self.size - 1:
                    self.tail = node_before_index
                node_before_index.next = node_before_index.next.next
                self.size -=1
        
        if self.size == 0:
            self.dummy_head = self.head = self.tail = None

        return


    def __str__(self):
        result = []
        curr = self.dummy_head.next
        while curr:
            result.append(str(curr.val))
            curr = curr.next
        return " -> ".join(result)



def main():
    my_ll = MyLinkedList()
    my_ll.addAtHead(3)
    my_ll.addAtTail(4)
    my_ll.addAtHead(2)
    my_ll.addAtHead(1)
    my_ll.addAtHead(0)
    print(my_ll)
    my_ll.deleteAtIndex(2)
    my_ll.deleteAtIndex(2)
    print(my_ll)
    my_ll.addAtIndex(3, 5)
    print(my_ll)
    my_ll.addAtIndex(3, 3)
    print(my_ll)
    my_ll.addAtIndex(3, 18)
    print(my_ll)

main()