# coding=utf8

__author__ = 'smilezjw'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, num):
        if num == []:
            return None
        medium = len(num) / 2
        # 每次选择数组中间的元素作为父结点，然后该元素左边的元素作为左子树，右边的元素作为右子树
        root = TreeNode(num[medium])
        root.left = self.sortedArrayToBST(num[:medium])
        root.right = self.sortedArrayToBST(num[medium+1:])
        return root

if __name__ == '__main__':
    num1 = [1, 2, 3, 5]
    num2 = [1, 3, 5, 7, 9]
    s = Solution()
    print s.sortedArrayToBST(num1)
    print s.sortedArrayToBST(num2)

#######################################################################################
# 构建平衡二叉查找树，对于已经排好序的数组而言，每次选择中间的元素作为父结点，然后该
# 元素左边的元素作为左子树，右边的元素作为右子树即可。
#