二叉树的所有题目都是基本的型的组合和变形,基本题:
1. 前中后序遍历
2. 求深度
3. 遍历树(按照一定规律返回所有元素,两棵树,遍历同时调整,遍历路径)
**** 

## bst第K大结点
1. 直接中序遍历，按照index返回结果。
2. 逆序中序遍历，提前返回。维护一个k。

## 序列化二叉树 ****

  这个题是真的恶心。结束的None的处理和结果中的None和null要匹配上。
  
## 重建二叉树
  前序或者后序+中序，恢复二叉树。
  
  递归的入参返回值如何设置？每次进入函数体，重建树，为根节点赋值。返回的树是上一级树的左子树和右子树
  
  知识点：递归
****

## 二叉树的深度
1. 递归求左右子树的最大深度，结果+1
2. 层序遍历

## 平衡二叉树
平衡二叉树:左右子树深度差值小于1.
1. 递归求左右子树深度，判断差值
2. 提前结束, 维护一种特殊情况
```python
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(root):
            if not root:
                return 0
            l = helper(root.left)
            if l == -1:
                return -1
            r = helper(root.right)
            if r == -1:
                return -1
            return max(l, r) + 1 if abs(l-r) < 2  else -1
        return helper(root) != -1
```
****

## 从上到下打印二叉树系列
  1. 从左到右，从上到下打印。
  2. 逐层打印，按层划分。
  3. 之字形打印。(双端队列不同顺序接收某一行的元素)
  
  知识点：双端队列 from collections import deque
  
## 树的子结构
  B树是不是A树的子树
  
  第一层遍历A树，找到和B根节点相等的节点
  第二层，再找到AB树相同的根节点后开始一起遍历两棵树，这一层是递归内容
  最终结果是：以A节点和B节点遍历 or 以A的子节点和B的节点遍历
  
  知识点：递归
  
## 二叉树的镜像 **
  注意利用python的平行赋值写法。
  root理解为地址，而不是值。如果地址内的值改变了，保存下来地址也不能保留原值。
  
  知识点：平行赋值

## 对称的二叉树
  关于根节点对称
  
  知识点：递归
  
## 二叉树中和为某一值的路径 *****
  做了一下午，检索到的路径存在path中，再将路径添加到输出结果中，后续递归改变path时，输出中的path会一同发生变化。
  
  知识点：回溯法和浅拷贝深拷贝。

## 二叉树的最近公共祖先 ****

1. bst:按照大小递归的搜索子树
2. 分情况讨论:都在左树返回公共祖先,右树返回None.都在右树返回公共祖先,左树返回None.左树返回左树元素,右树返回右树元素,则返回根节点为公共祖先.
```python
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or p.val == root.val or q.val == root.val:
            return root  # 当root为空就返回空,是其中要找的某一个节点,就返回这个节点
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if not l:
            return r
        if not r:
            return l
        return root
```
