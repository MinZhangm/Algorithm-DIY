# 98
# 判断是不是二叉搜索树

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def helper(root, low, high):
            if not root:
                return True
            
            val = root.val
            if val <= low or val >= high:
                return False
            
            # 重点就在这里的交换，先来判断了右子树是否是搜索树，此时上界交换成了根节点的值，而下界是当前根节点的值，这就是对于当前根节点的右子树的判断条件。
            if not helper(root.right, val, high):
                return False
            if not helper(root.left, low, val):
                return False
            return True
        ans = helper(root, float('-inf'), float('inf'))
        return ans
