# 输入：无序链表
# 输出：排序后的链表
# nlogn，常数级空间

# 归并排序
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid, slow.next = slow.next, None

        l, r = self.sortList(head), self.sortList(mid)

        res = ListNode(0)
        ans = res
        while l and r:
            if l.val < r.val:
                tmp = l
                l = l.next
                tmp.next = None
                res.next = tmp
            else:
                tmp = r
                r = r.next
                tmp.next = None
                res.next = tmp
            res = res.next
        res.next = l if l else r
        return ans.next
