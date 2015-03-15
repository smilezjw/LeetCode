# coding=utf8

__author__ = 'smilezjw'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 对二叉搜索树进行中序遍历，由于左子树的结点值小于根结点值，右子树的结点值都大于根结点值
    # 因此中序遍历得到的结点值肯定是递增的
    # def isValidBST(self, root):
    #     stack = []
    #     value = []  # 用来记录中序遍历的结点的值
    #     while root or stack:
    #         if root:
    #             stack.append(root)
    #             root = root.left
    #         else:
    #             root = stack.pop()
    #             # 判断中序遍历的结点的值是否递增，如果不是递增则不符合二叉查找树的条件
    #             if len(value) == 0 or root.val > value[-1]:
    #                 value.append(root.val)
    #             else:
    #                 return False
    #             root = root.right
    #     return True


    # 解法二：主要考虑结点的值的规律
    # 左子树的所有结点值都小于根结点的值，右子树所有结点值都大于根结点的值
    def validBST(self, root, min, max):
        if root is None:
            return True
        if root.val <= min or root.val >= max:
            return False
        return self.validBST(root.left, min, root.val) and self.validBST(root.right, root.val, max)

    def isValidBST(self, root):
        min = -2**31-1  # 注意这里的最小值和最大值的范围
        max = 2**31
        return self.validBST(root, min, max)

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(1)
    print s.isValidBST(root)

#####################################################################################
# 这道题采用两种方法求解。
# 方法一是中序遍历二叉查找树，将中序遍历结点的值记录下来，判断中序遍历结点的值是否递增。
# 方法二是深度优先搜索判断每个结点的值的范围，例如下面一个二叉查找树：
#                     3
#                   /   \
#                  2     6
#                /     /   \
#               1     5     7
# 左子树的结点值在（负无穷，3）范围内，右子树的结点值在（3，正无穷）范围内。
# 