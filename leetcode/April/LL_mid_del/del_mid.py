def deleteMiddle(self, head):
    if head.next is None:
        return head
    
    slower_pointer, faster_pointer = head, head.next
    slower_moves = False

    while faster_pointer.next is not None:
        faster_pointer = faster_pointer.next
        if slower_moves:
            slower_pointer = slower_pointer.next
            slower_moves = False
        else:
            slower_moves = True

    slower_pointer.next = slower_pointer.next.next

    return head





