# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        next_val = self.next.val if self.next else None
        return f"Node(val={self.val}, next={next_val})"

def reorderList(head) -> None:
    # Last is the node that we'll transport to be an insertee's next node 
    # New tail is the node that we'll cut off from 'last' after transporting
    insertee = head
    last = head
    stack = []

    while last.next is not None:
        stack.append(last)
        last = last.next

    constant_len = len(stack)

    while len(stack) > (constant_len + 1) // 2:
        new_tail = stack.pop()
        last = new_tail.next

        # Transport last, cut new tail
        last.next = insertee.next
        insertee.next = last
        new_tail.next = None
        # insertee is now the next node after inserted one
        insertee = last.next

    
def main():
    head = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    node_5 = ListNode(5)
    head.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    nodes = [head, node_2, node_3, node_4, node_5]


    reorderList(head)
    print(nodes)

main()

