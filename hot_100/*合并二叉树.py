# 输入两颗二叉树，共存相加，不共存保留存在的分支
# 返回合并后的二叉树

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return t1
        if t1 and t2:
            t1.val = t1.val + t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
        if not t1 and t2:
            t1 = t2
        return t1
# t1缺失，可以直接通过=进行二叉树节点的复制操作，仍然还能保留前后的位置关系。
