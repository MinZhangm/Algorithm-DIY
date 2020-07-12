# 输入:矩阵,0表示水,1表示岛屿,只有上下左右才是相连的陆地
# 输出:岛屿的数量

# 深度搜索的次数
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def helper(i, j):
            
            grid[i][j] = '0'
            for x, y in forward:
                while 0 <= i + x <n and 0 <= j + y < m and grid[i+x][j+y] == '1':
                    helper(i+x, j+y)
            return 

        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        res = 0

        # 深度优选搜索的次数就是岛屿的数量
        forward = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    res += 1
                    helper(i, j)
        return res
