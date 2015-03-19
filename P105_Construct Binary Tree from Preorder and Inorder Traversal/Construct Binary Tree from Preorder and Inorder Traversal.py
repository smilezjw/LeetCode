# coding=utf8

__author__ = 'smilezjw'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        # 直接用列表进行递归，结果是对的，可是Leetcode现在会报Memory Limit Exceed
        # if inorder == []:
        #     return None
        # root = TreeNode(preorder[0])
        # rootPos = inorder.index(root.val)
        # root.left = self.buildTree(preorder[1:rootPos+1], inorder[:rootPos])
        # root.right = self.buildTree(preorder[rootPos+1:], inorder[rootPos+1:])
        # return root

        if preorder == inorder == []:
            return None
        return self.build(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1)

    def build(self, preorder, inorder, preStart, preEnd, inStart, inEnd):
        # 引入4个参数分别控制先序遍历列表的左右子树结点索引范围和中序遍历列表的左右子树结点索引范围
        if preStart > preEnd:
            return None
        root = TreeNode(preorder[preStart])
        rootIndex = inorder.index(root.val)
        # 左孩子的先序遍历列表结点范围，preStart + 左孩子的个数（rootIndex - inStart）
        root.left = self.build(preorder, inorder, preStart+1, preStart + rootIndex - inStart, inStart, rootIndex-1)
        # 右孩子的先序遍历列表结点范围，从后往前，preEnd + 1 - 右孩子个数(inEnd - rootIndex)
        root.right = self.build(preorder, inorder, preEnd - (inEnd - rootIndex) + 1, preEnd, rootIndex+1, inEnd)
        return root

if __name__ == '__main__':
    s = Solution()
    #print s.buildTree([1, 2, 3], [2, 3, 1])
    print s.buildTree([3, 2, 1, 4, 5], [1, 2, 3, 4, 5])
    print s.buildTree([5, 4, 1, 2, 3], [1, 2, 3, 4, 5])
    print s.buildTree([3, 2, 1, 5, 6], [2, 3, 5, 1, 6])

########################################################################################
# 这道题烦人之处在于，明明可以直接递归传递列表分片参数，却报错Memory Limit Exceed，非要
# 用4个参数自己控制左右孩子在先序和中序遍历列表中的索引范围。
# 已知二叉树的中序和先序序列构造二叉树，思路如下：
# 1.树的根结点为先序遍历的第一个元素；
# 2.找出根结点在中序遍历中的位置，根结点左边的所有元素为左子树；根结点右边的所有元素为
# 右子树。如果根结点左边或者右边元素为空，则该结点的左子树或右子树为空。
# 3.递归求解二叉树。
#