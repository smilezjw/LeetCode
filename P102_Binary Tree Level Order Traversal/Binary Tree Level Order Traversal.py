# coding=utf8

__author__ = 'smilezjw'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        queue = {0: [root]}  # 用字典记录每一层的结点，键为二叉树的层数，值为该层的结点
        res = []   # 按照要求记录每一层结点的值
        level = 0  # 二叉树的层数
        while level in queue:
            levelValue = []
            for curr in queue[level]:   # 遍历该层结点
                levelValue.append(curr.val)  # 记录该层的结点的值
                if curr.left:
                    if level+1 not in queue:
                        queue[level+1] = [curr.left]  # 记录下一层结点
                    else:
                        queue[level+1].append(curr.left)
                if curr.right:
                    if level+1 not in queue:
                        queue[level+1] = [curr.right]
                    else:
                        queue[level+1].append(curr.right)
            res.append(levelValue)
            level += 1  # 遍历下一层
        return res

    def preOrder(self, root, level, res):
        # 这里采用深度递归，先序遍历，用变量level记录结点所在的层数
        # 正好level从0开始对应列表的下标
        if root:
            if len(res) < level+1:    # 注意这里的判断条件，因为层数从0开始
                res.append([])
            res[level].append(root.val)
            self.preOrder(root.left, level+1, res)
            self.preOrder(root.right, level+1, res)

    def levelOrderDFS(self, root):
        res = []
        self.preOrder(root, 0, res)
        return res

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    p = root
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root = root.right
    root.left = TreeNode(15)
    root.right = TreeNode(7)
    print s.levelOrder(p)
    print s.levelOrderDFS(p)

####################################################################################
# 这道题采用两种方法。第一种方法用字典{层数:该层对应的结点}键值对，遍历每一层的结点，
# 用列表记录该层结点的值；同时记录下一层结点。直至完成遍历整棵树。
# 第二种方法用深度递归，这里用先序遍历二叉树，同时用变量level记录层数，根结点的层数为0。
#