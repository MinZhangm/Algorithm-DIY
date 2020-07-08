## 编程
1. 求解对字符串进行哈夫曼编码后，二进制位数

哈弗曼树,
带权路径最小的树，路径指的是从根节点到叶子结点的距离.
带权路径和是所有节点的权和路径长度之积的和.
权值就是这个节点的字符出现的频率.

```python
  class TreeNode(object):
      def __init__(self, val):
          self.val = val
          self.left = None
          self.right = None

  class huffman(object):
      def dis(self, s):
          # 统计词频
          n = len(s)
          if not s:
              return 0
          dict = {}
          for i in range(n):
              if s[i] not in dict:
                  dict[s[i]] = 0
              dict[s[i]] += 1
          s_dict = sorted(dict.items(), key=lambda item:item[1])
          # res是哈夫曼树的根节点
          def cons(d):
              if len(d) <= 1:
                  if not d:
                      return TreeNode(None)
                  else:
                      if len(d[0]) > 2:
                          return d[0][2]
                      else:
                          return TreeNode(d[0][1])

              root = TreeNode(1)
              if d[0][1] < d[1][1]:
                  if len(d[0]) > 2:
                      root.left = d[0][2]
                  else:
                      root.left = TreeNode(d[0][0])
                  if len(d[1]) > 2:
                      root.right = d[1][2]
                  else:
                      root.right = TreeNode(d[1][0])
              else:
                  if len(d[0]) > 2:
                      root.right = d[0][2]
                  else:
                      root.right = TreeNode(d[0][0])
                  if len(d[1]) > 2:
                      root.left = d[1][2]
                  else:
                      root.left = TreeNode(d[1][0])
              root.val = str(d[0][1] + d[1][1])
              d.append((root.val, d[0][1] + d[1][1], root))
              d = d[2:]
              d = sorted(d, key=lambda item:item[1])
              root = cons(d)
              return root

          res = cons(s_dict)
          ans = {}

          # list_node = []
          # children = [res]
          # while children:
          #     tmp = []
          #     for i in children:
          #         list_node.append(i.val)
          #         if i.left:
          #             tmp.append(i.left)
          #         if i.right:
          #             tmp.append(i.right)
          #     children = tmp
          # print(list_node)

          def helper(node, tmp):
              if not node:
                  return
              elif node and not node.left and not node.right:
                  ans[node.val] = tmp
                  return

              helper(node.left, tmp+1)
              helper(node.right, tmp+1)

          helper(res, 0)
          # print(ans)
          out = 0
          for i in range(len(s)):
              out += ans[s[i]]
          return out

  solution = huffman()
  print(solution.dis('espressif'))
```

2. 魔法币

初始没有金币，第一个箱子输入x个金币，返回2x+2个；第二个箱子输入x个金币，返回2x+1个。为了集齐n个金币，投入箱子的顺序。
```python
import sys 
n = int(sys.stdin.readline().strip())
res = ''
while n > 0:
  if n %2 == 0:
    n = (n-2)/2
    res = '2 + res
  else:
    n = (n-1)/2
    res = '1' + res
 return res
```
## 简答
1.当神经网络中有不可导的函数的时候，怎么办？

  次梯度：relu中的x=0的点。x>0时，梯度为1；x<0时，梯度为0.次梯度就是在左右临界的可导点的导数之间随机的取一个值，[0, 1].
  
  重参数：对符合(/mui, /sigmoid)分布的高斯分布进行采样是不可导的，所以就对标准的高斯分布进行采样，然后进行缩放，这样就可导了？？？？（没理解）
  
  https://zhuanlan.zhihu.com/p/97465608
  
2.常见的分类的损失函数有哪些？原理。

https://blog.csdn.net/weixin_41065383/article/details/89413819

## 单选
1. 矩阵的计算量，如果N1(w, x) N2(x, y) N3(y, z),wxyz需要满足什么样的条件才能使得：计算量(N1@N2)@N3 < N1@(N2@N3)?
  
  x(wy)+y(wz) < y(xz) + x(wy)

2.冒泡排序。
