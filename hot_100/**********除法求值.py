# 输入，计算式，计算式结果，待求计算式
# 输出：待求计算式结果

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for (x, y), v in zip(equations, values):
            if x not in graph:
                graph[x] = {y: v}
            else:
                graph[x][y] = v
            if y not in graph:
                graph[y] = {x: 1.0/v}
            else:
                graph[y][x] = 1.0 / v
        
        def helper(x, y):
            if x not in graph:
                return -1
            elif x == y:
                return 1
            else:
                for i in graph[x].keys():
                    if i == y:
                        return graph[x][i]
                    elif i not in visited:
                        visited.add(i)                    # 如果访问过，那么就直接跳过
                        res = helper(i, y)
                        if res != -1:
                            return res * graph[x][i]
                return -1
        res = []
        for (x, y) in queries:
            visited = set()
            res.append(helper(x, y))
        return res
