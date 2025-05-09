class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        next_val = self.next.val if self.next else None
        self_val = self.val
        return f'Node:val={self_val}, next={next_val}'
    

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:

    dummy = ListNode(0)
    tail = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 or list2
    return dummy.next



def main():
    list11 = ListNode(val=1)
    list12 = ListNode(val=2) 
    list13 = ListNode(val=4)
    list11.next, list12.next = list12, list13

    list21 = ListNode(val=1) 
    list22 = ListNode(val=3) 
    list23 = ListNode(val=4) 
    list21.next, list22.next = list22, list23

    mergeTwoLists(list11, list21)



main()