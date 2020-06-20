基本题：
1. 删除节点
2. 增加节点
3. 调整节点顺序
4. 双链表


## 删除节点，增加节点
1. 按照val删除节点（双指针，pre和cur）
2. 按照index删除节点（正数的index和倒数的index）
```python
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        former, later = head, head
        for _ in range(k):
            if later:
                later = later.next
            else:
                return ListNode(None)
        
        while former and later:
            former = former.next
            later = later.next
        return former
```

## 调整节点
1. 复制链表(复杂的链表借助哈希) *****
2. 倒序

## 双链表
1. 两个链表的第一个公共节点 ******
```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB
        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA
        return node1
```
