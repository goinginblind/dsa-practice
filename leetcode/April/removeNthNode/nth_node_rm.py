def removeNthFromEnd(self, head, n: int):
    # Traverse the whole list and put every node into HashMap
    node_map, curr_node_index = {}, 0  # Indexing is 1-based
    ptr = head
    while ptr:
        curr_node_index += 1
        node_map[curr_node_index] = ptr
        ptr = ptr.next 
    # Get [max_index - n] positioned node
    if curr_node_index - n > 0:
        node_rewire = node_map[curr_node_index - n]
        # Rewire this node to the next after the one we're removing
        node_rewire.next = node_rewire.next.next
    # Elif the first node needs to be removed setup a new head
    elif curr_node_index - n == 0:
        head = head.next
    # Done! Return the head of the LL
    return head
