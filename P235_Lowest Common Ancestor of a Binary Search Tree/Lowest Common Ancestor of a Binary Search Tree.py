# coding=utf8

__author__ = 'smilezjw'


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        # 若p和q分别位于某结点两侧，或者p或q的值与该结点值相同，则该结点为p和q的最近公共祖先
        if (p.val - root.val) * (q.val - root.val) <= 0:
            return root
        # 否则p和q都位于某结点左侧，则最近公共祖先结点在左子树中查找
        elif root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # 否则，最近公共祖先结点在右子树中查找
        else:
            return self.lowestCommonAncestor(root.right, p, q)