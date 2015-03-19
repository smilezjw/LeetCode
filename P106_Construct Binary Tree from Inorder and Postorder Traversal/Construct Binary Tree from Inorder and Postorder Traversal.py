# coding=utf8

__author__ = 'smilezjw'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        # 同样的memory limit exceed
        # if inorder == []:
        #     return None
        # root = TreeNode(postorder[-1])
        # rootIndex = inorder.index(root.val)
        # root.left = self.buildTree(inorder[:rootIndex], postorder[:rootIndex])
        # root.right = self.buildTree(inorder[rootIndex+1:], postorder[rootIndex:-1])
        # return root

        if inorder == postorder == []:
            return None
        return self.build(inorder, postorder, 0, len(inorder)-1, 0, len(postorder)-1)

    def build(self, inorder, postorder, inStart, inEnd, postStart, postEnd):
        if postStart > postEnd:
            return None
        root = TreeNode(postorder[postEnd])
        rootIndex = inorder.index(root.val)
        # 左孩子的后序遍历列表结点范围，postStart + 左孩子的个数（rootIndex - inStart, 由于从0开始所以还要减1（上一题先序的第0位就是根结点所以不用减1）
        # 右孩子的后序遍历列表结点范围，从后往前，preEnd - 右孩子个数(inEnd - rootIndex)，最后一位就是根结点
        root.left = self.build(inorder, postorder, inStart, rootIndex-1, postStart, postStart+(rootIndex-inStart)-1)
        root.right = self.build(inorder, postorder, rootIndex+1, inEnd, postEnd-(inEnd-rootIndex), postEnd-1)
        return root

if __name__ == '__main__':
    s = Solution()
    print s.buildTree([1, 2, 3], [3, 2, 1])
    print s.buildTree([3, 2, 1, 4, 5], [1, 2, 3, 4, 5])

##########################################################################################
# 和上一题是一样的，就是要注意后序的左右子树的索引范围。
#