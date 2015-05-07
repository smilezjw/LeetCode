# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def canFinish(self, numCourses, prerequisites):
        # inNodes记录每个结点的入度，如果该结点入度大于0的话
        inNodes = {}
        for pair in prerequisites:
            if pair[0] not in inNodes:
                inNodes[pair[0]] = [pair[1]]
            # 在测试数据集中出现了重复的数据，如[1,9], [1,9]，这里避免重复
            elif pair[1] not in inNodes[pair[0]]:
                inNodes[pair[0]].append(pair[1])
        # 找到入度为0的结点
        singleNode = [i for i in xrange(numCourses) if i not in inNodes]
        while singleNode:
            node = singleNode.pop(0)
            # 对入度为0的结点，将其指向其他结点的边一同删去
            for innode in inNodes.keys():
                if node in inNodes[innode]:
                    inNodes[innode].remove(node)
                # 然后找到删去后新的入度为0的结点
                if len(inNodes[innode]) == 0:
                    singleNode.append(innode)
                    del inNodes[innode]
        # 如果不存在环，则最后所有结点都被删去，字典长度为0
        return len(inNodes) == 0

if __name__ == '__main__':
    s = Solution()
    print s.canFinish(2, [[1, 0]])
    print s.canFinish(2, [[1, 0], [0, 1]])
    print s.canFinish(4, [[1, 0], [2, 1], [3, 0], [3, 2]])
    print s.canFinish(4, [[1, 0], [2, 1], [0, 3], [3, 2]])

    print s.canFinish(10, [[5,8],[3,5],[1,9],[4,5],[0,2],[1,9],[7,8],[4,9]])

############################################################################################
# 这道题考察的是有向图的拓扑排序。在一个表示工程的有向图中，用结点表示活动，用边表示活动之间
# 的优先关系，该有向图成为AOV网，Active On Vertex Network.
# 对AOV网进行拓扑排序的方法：从AOV网中选择一个没有前趋的结点，即该结点的入度为0，从AOV网中删除
# 该结点并且删去从该结点出发的有向边，然后判断得到新的入度为0的结点重复上述步骤，直到网中没有
# 入度为0的顶点为止。如果有向图中存在环，则最后网中一定剩余结点，否则网中没有结点。
#
