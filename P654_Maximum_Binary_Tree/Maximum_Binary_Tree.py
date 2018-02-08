# coding=utf8


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        sortedNum = sorted(nums)[::-1]
        root = TreeNode(sortedNum[0])
        idx = nums.index(sortedNum[0])
        left = nums[:idx]
        right = nums[idx+1:]
        if left and len(left) > 0:
            root.left = self.constructMaximumBinaryTree(left)
        if right and len(right) > 0:
            root.right = self.constructMaximumBinaryTree(right)
        return root

    def printTree(self, root):
        if root:
            print(str(root.val) + ' - ')
            self.printTree(root.left)
            self.printTree(root.right)
        print('- None -')


if __name__ == '__main__':
    solution = Solution()
    root = solution.constructMaximumBinaryTree([3,2,1,6,0,5])
    solution.printTree(root)
