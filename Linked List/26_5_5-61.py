"""
61. 旋转链表

给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。

链表中节点的数目在范围 [0, 500] 内
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        n = 1
        now = head
        while now.next:
            now = now.next
            n += 1
        now.next = head
        k = k % n
        new = head
        for _ in range(n - k - 1):
            new = new.next
        newhead = new.next
        new.next = None
        return newhead
