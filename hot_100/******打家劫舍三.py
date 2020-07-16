# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def helper(root):
            if not root:
                return 0, 0             # 不偷根节点左右支路的最大的和，投了根节点左右支路的和，这两中情况中取最大就是最终的结果
            l_n, l = helper(root.left)
            r_n, r = helper(root.right)
            return max(l_n, l) + max(r_n, r), root.val + l_n + r_n

        return max(helper(root))

