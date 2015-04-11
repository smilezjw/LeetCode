# coding=utf8

__author__ = 'smilezjw'


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # 深度优先搜索193ms
    def cloneGraph_DFS(self, node):
        def dfs(input, map):
            if input in map:
                return map[input]  # 如果结点已经有对应的新建的节点，则直接返回新建的节点
            output = UndirectedGraphNode(input.label)  # 构建一个节点，该节点的值和原图中的节点的值一样
            map[input] = output  # 将新建的节点映射到原图中的节点上去
            for neighbor in input.neighbors:  # 其实上面这几步就是在复制节点
                output.neighbors.append(dfs(neighbor, map))  # 这一步是在对每个output结点复制其对应的原图中input节点的邻居
            return output

        if node is None:
            return None
        return dfs(node, {})

    # 宽度优先搜索182ms
    def cloneGraph_BFS(self, node):
        if node is None:
            return None
        queue = []  # 用队列进行宽度优先搜索
        map = {}
        newNode = UndirectedGraphNode(node.label)
        queue.append(node)
        map[node] = newNode
        while queue:
            curr = queue.pop()
            for neighbor in curr.neighbors:  # 每次都把curr对应的新建节点的邻居结点添加完成，再换下一个结点
                if neighbor not in map:      # 如果curr的邻居还没有遍历过：
                    copy = UndirectedGraphNode(neighbor.label)  # 首先新建一个节点使该节点的值与原图中curr的邻居节点的值相等
                    map[curr].neighbors.append(copy)            # 然后将该新建节点添加到curr对应的节点的邻居节点中
                    map[neighbor] = copy                        # 将原图中对应节点映射到该新建节点
                    queue.append(neighbor)                      # 将原图中对应节点添加到待遍历队列中
                else:                         # 如果curr的邻居已经遍历过
                    map[curr].neighbors.append(map[neighbor])   # 直接将该邻居节点映射的新建节点添加到curr对应的节点的邻居节点中
        return newNode


if __name__ == '__main__':
    s = Solution()
    node = UndirectedGraphNode(1)
    node.neighbors = [UndirectedGraphNode(0), UndirectedGraphNode(2)]
    p = node.neighbors[0]
    q = node.neighbors[1]
    p.neighbors = [node, q]
    q.neighbors = [node, p, q]
    print s.cloneGraph_DFS(node)
    print s.cloneGraph_BFS(node)

############################################################################################
# 遍历图可以采用深度优先搜索或者宽度优先搜索，因此深拷贝一个图也可以采用这两种方法。无论是
# 深度优先还是宽度优先都需要一个哈希表来存储原图中的节点和新图中的节点的一一映射关系。
# 看过上面深度优先搜索和宽度优先搜索的代码后，觉得还是挺好理解的。
#