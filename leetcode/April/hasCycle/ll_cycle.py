def hasCycle(head) -> bool:
    pointers = set()
    node = head
    while node:
        if node.next in pointers:
            return True
        pointers.add(node)
        node = node.next
    
    return False