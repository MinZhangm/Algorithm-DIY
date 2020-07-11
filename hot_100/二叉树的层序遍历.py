# 输出二叉树的层序遍历

# 使用上端队列，每次进入while的时候都取一次当前的children的长度，就是目前这一层的所有节点的数目，然后遍历这些当前层上的所有节点
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        children = deque()

        res = []
        if not root:
            return res
        children.append(root)
        while children:
            l = len(children)
            tmp_res = []
            for i in range(l):
                node = children.popleft()
                tmp_res.append(node.val)
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            res.append(tmp_res)
        return res
# 使用深度优先搜索也可以做
# 将是同一深度的节点方到相同的列表的子列表中去
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []

        def helper(root, level):
            if not root:
                return
            if level > len(res) -1:
                res.append([])
            tmp = res[level]
            tmp.append(root.val)
            res[level] = tmp
            helper(root.left, level+1)
            helper(root.right, level+1)
            return 

        helper(root, 0)
        return res
