# 梯度下降求解网络的参数
# 逻辑回归，最大似然函数做目标函数，sigmiod做激活函数，学习率0.01，w初始化为0，迭代10次
# 结果保留5位有效数字
# 每天推一推强壮中国人！

class Solution:
    def calc_weight(self, x, y):
        # write code here
        import math
        import numpy as np

        iter_num = 10
        lr = 0.01
        n = len(x)

        x = np.array(x).astype(np.float)
        y = np.array(y).astype(np.float)
        w = 0.0

        for _ in range(iter_num):
            grad = 0
            for num in range(n):
                grad += (-1 * (y[num]) * x[num] + x[num] * math.exp(w*x[num]) / (1.0 + math.exp(x[num] * w)))
            w = w - lr * grad
        return round(w, 5)


Solution = Solution()
print(Solution.calc_weight([-10, -9, -5, 2, 4, 5], [0, 0, 0, 1, 1, 1]))
