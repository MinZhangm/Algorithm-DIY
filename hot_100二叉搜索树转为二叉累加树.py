# 输入：树
# 输出：当前节点的值为这个节点的原始值+所有比他大的节点的值。
# 维护一个变量，保存所有大于当前节点的节点值之和。

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def helper(root, sub):
            if not root:
                return None, sub

            root.right, sub = helper(root.right, sub)
            root.val += sub
            sub = root.val
            root.left, sub = helper(root.left, sub)
            return root, sub
        root, _ = helper(root, 0)
        return root
