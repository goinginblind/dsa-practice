# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def deleteNode(self, node):
    current_node = self.head.next
    previous_node = self.head
    while current_node.next is not None:
        if current_node.val == node.val:
            previous_node.next = current_node.next
        previous_node = current_node
        current_node = current_node.next

         
        