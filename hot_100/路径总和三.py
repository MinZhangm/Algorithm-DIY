# 输入：树，目标总和
# 返回：路径总和符合目标值的路径的数目，路径起始节点不一定非得是根节点，路径终点也不一定非得是叶子结点

# mycode，双重递归，一层递归找以当前根节点为路径起点符合目标总和的路径计数，第二层递归是分别以树中的左右节点作为根节点检索路径总和为目标总和的数目。
class Solution:
    def __init__(self):
        self.count = 0
    def pathSum(self, root: TreeNode, sum: int) -> int:

        def helper(node, tgt):
            if not node:          
                return 

            tgt = tgt - node.val
            if tgt == 0:
                self.count += 1

            helper(node.left, tgt)
            helper(node.right, tgt)
            return 
        
        if not root:
            return self.count
        helper(root, sum)
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)
        return self.count     
       
# 一层递归
# 维护一个list，将新的节点添加进去，每次都重新计算新的满足目标总和的数目

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def helper(root, l):
            if not root:
                return 0
            count = 0
            l = [root.val + i for i in l]
            l.append(root.val)
            for i in l:
                if i == sum:
                    count += 1
            return count + helper(root.left, l) + helper(root.right, l)
        return helper(root, [])
