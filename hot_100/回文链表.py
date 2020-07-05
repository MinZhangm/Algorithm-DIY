# 输入：链表
# 输出：判断是否是回文链表

# 将链表元素入栈，然后弹栈与链表中的元素一样对比。
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        node = head
        while head:
            stack.append(head.val)
            head = head.next
        for i in stack[::-1]:
            if not i == node.val:
                return False
            node = node.next
        return True
        
# 快慢指针 + 一半的栈
# 使用快快慢指针找到整个链表的中点，奇数时，s指向正中间，偶数时，s指向第二半的开始元素。
# f为None的时候是偶数，f and not f时是奇数。
# 保证s指向的是回文段的第一个元素。

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # half堆栈
        # 快慢指针，找到链表的在中间位置，奇数是正中间，偶数是第二半的开始
        s = head
        f = head
        stack = []
        while f and f.next:
            stack.append(s.val)
            s = s.next
            f = f.next.next
        if f:  # 当f存在，但是f.next为none的时候，整个链表有奇数个元素，如果是f为None，就有偶数个元素
            s = s.next  # 保证s是从指向回文的第一个元素开始
        while stack:
            tmp = stack.pop()
            if tmp != s.val:
                return False
            s = s.next
        return True
