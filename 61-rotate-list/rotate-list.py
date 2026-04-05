# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(head==None or k==0 or head.next==None):
            return head
        length=1
        temp=head
        while temp.next:
            temp=temp.next
            length+=1
        temp.next=head
        k=k%length
        n=abs(length-k-1)
        new_tail=head
        for i in range(n):
            new_tail=new_tail.next
        new_head=new_tail.next
        new_tail.next=None
        return new_head