# 输入链表
# 输出反转后的结果

# 迭代
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        tmp = head.next
        res = head
        res.next = None
        head = tmp

        while head:
            tmp = head
            head = head.next
            tmp.next = res
            res = tmp
        return res
        
# 递归
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def helper(f, c):
            if f and not c:
                f.next = None
                return f, f
            l, r = helper(c, c.next)
            f.next = None
            r.next = f
            return l, f
        
        if not head:
            return None

        l, r = helper(head, head.next)
        return l
