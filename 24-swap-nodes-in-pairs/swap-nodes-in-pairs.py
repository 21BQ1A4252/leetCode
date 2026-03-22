# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head==None or head.next==None):
            return head
        temp=head
        while(temp!=None and temp.next!=None):
            a=temp.val
            temp.val=temp.next.val
            temp.next.val=a
            temp=temp.next.next
        return head


        