# 输入：链表，last是环形一端，pos是结尾指向的indx
# 输出：是否是环形链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        s = head
        f = head.next
        while s != f:

            if not s or not f:
                return False
            if f.next:
                f = f.next.next
            else:
                return False
            s = s.next
        return True
 # 尤其需要注意一种，当pos=-1是，不是环形链表。
 # 当按照next对链表进行遍历的时候，出现了None那就不是环形链表
 # 虽然pos是-1，但是对链表的最后一个node.next时仍然返回None
 # if not f.next: return False
 # 否则会出现s和f都为None，导致pos=-1时出现错误的结果
