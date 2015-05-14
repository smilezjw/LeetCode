# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def findOrder(self, numCourses, prerequisites):
        inNodes = {}
        for pair in prerequisites:
            if pair[0] not in inNodes:
                inNodes[pair[0]] = [pair[1]]
            elif pair[1] not in inNodes[pair[0]]:
                inNodes[pair[0]].append(pair[1])
        # 找到入度为0的结点
        singleNode = [i for i in xrange(numCourses) if i not in inNodes]
        order = []
        while singleNode:
            node = singleNode.pop(0)
            order.append(node)
            # 对入度为0的结点，将其指向其他结点的边一同删去
            for innode in inNodes.keys():
                if node in inNodes[innode]:
                    inNodes[innode].remove(node)
                 # 然后找到删去后新的入度为0的结点
                if len(inNodes[innode]) == 0:
                    singleNode.append(innode)
                    del inNodes[innode]
        # 如果不存在环，则最后所有结点都被删去，字典长度为0
        return order if len(inNodes) == 0 else []

if __name__ == '__main__':
    s = Solution()
    print s.findOrder(2, [[1, 0]])
    print s.findOrder(2, [[1, 0], [0, 1]])
    print s.findOrder(4, [[1, 0], [2, 1], [3, 0], [3, 2]])
    print s.findOrder(4, [[1, 0], [2, 1], [0, 3], [3, 2]])

    print s.findOrder(10, [[5,8],[3,5],[1,9],[4,5],[0,2],[1,9],[7,8],[4,9]])

#####################################################################################
# 这道题在P207的基础上修改一下即可，题目只要求返回任意一种拓扑排序即可，而不是所有
# 可能的拓扑排序情况。采用宽度优先搜索，用列表来进行队列操作记录入度为0的结点。
#