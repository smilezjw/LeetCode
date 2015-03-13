# coding=utf8

__author__ = 'smilezjw'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        return self.dfs(1, n)

    def dfs(self, start, end):
        if start > end:
            return [None]
        res = []  # 每次递归深入都重新初始化res
        for rootval in xrange(start, end+1):    # 从start到end中依次选取一个值作为根结点的值
            leftTree = self.dfs(start, rootval-1)  # 则左子树由start到rootval-1构成
            rightTree = self.dfs(rootval+1, end)   # 则右子树由rootval+1到end构成
            for i in leftTree:  # 左子树列表中记录左子树或者一个左孩子结点或者[None]
                for j in rightTree:  # 右子树列表中记录右子树或者一个右孩子结点或者[None]
                    root = TreeNode(rootval)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res

if __name__ == '__main__':
    s = Solution()
    print s.generateTrees(2)

#######################################################################################
# 这道题和上一道题P96思路相似，但是这道题需要枚举出所有的解法，因此需要用深度优先搜索。
# 从start到end中依次选择一个结点作为根结点，然后左子树由start到rootval-1构成，右子树由
# rootval+1到end构成。还是需要走一下流程例如n=2。
#