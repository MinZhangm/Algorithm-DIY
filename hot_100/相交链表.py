# 输入链表
# 输出共有的第一个节点，如果灭有返回None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l = headA
        r = headB
        while  l != r:
            l = l.next if l else headB
            r = r.next if r else headA
        return l
# 确定什么时间交换
# 0, [1,3], [], 2, 0
# 其中只要有一个移动到空，也判断，移动到空判断之后，再交换。
