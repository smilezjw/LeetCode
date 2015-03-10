# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        l1 = list(s1)  # 注意这些判断条件还是要的，不然大数据集会TLE
        l2 = list(s2)
        l1.sort()
        l2.sort()
        if l1 != l2:
            return False
        length = len(s1)
        for i in xrange(1, length):
            # s1的左边部分等于s2的左部分，并且s1的右部分等于s2的右部分
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            # s1的左部分等于s2的右部分，并且s1的右部分等于s2的左部分
            if self.isScramble(s1[:i], s2[length-i:]) and self.isScramble(s1[i:], s2[:length-i]):
                return True
        return False

if __name__ == '__main__':
    s = Solution()
    print s.isScramble('great', 'rgtae')

###########################################################################################
# 这道题是二叉树的题目，这里用递归求解。求解思路主要是判断两种情况：
# 1、如果s1的左部分等于s2的左部分，并且s1的右部分等于s2的右部分；
# 2、如果s1的左部分等于s2的右部分，并且s1的右部分等于s2的左部分；
# 这两种情况都是符合scramble的规则。对于s1任意位置划分左右部分，递归成立的话则返回True，否则
# 返回False。
# 这道题还是很难的，还可以用三维动态规划求解 = =
#