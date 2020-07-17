# 输入：列表，元素还是列表，每一个元素[h, k],h表示当前位置上的人的身高,k表示队列中在他前面比他高的人数有多少
# 输出：根据信息进行排列后的队列情况

# 解决思路：先对所有人的身高从大到小排序，同时相同身高的人，按照k从小到大排序
# 每次从左到右取出一个，按照以k为idx进行插入

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        return output

# 为什么这么做？怎么想到的？？
