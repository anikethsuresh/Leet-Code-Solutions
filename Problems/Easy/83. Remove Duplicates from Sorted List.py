"""

83. Remove Duplicates from Sorted List

Since the linked list is sorted, you only need to walk through the list and further traverse it if the element is repeated.
Very simple question
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        else:
            current = head
            while current != None: 
                next_node = current.next
                while next_node!= None:
                    if current.val != next_node.val:
                        break
                    next_node = next_node.next
                current.next = next_node
                current = current.next
        return head
        

