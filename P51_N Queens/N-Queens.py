# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def solveNQueens(self, n):
        def check(k, j):  # 判断第k个Queen是否可以放在第j列
            for i in xrange(k):
                # 检查和之前的Queens是否列冲突或者对角线冲突
                if board[i] == j or abs(k - i) == abs(board[i] - j):
                    return False
            return True

        def dfs(depth, valuelist):
            if depth == n:  # depth记录第几个Queen，从0开始
                res.append(valuelist)
                return
            for i in xrange(n):
                if check(depth, i):
                    board[depth] = i  # 第depth个Queen处于第i列
                    s = '.' * n
                    dfs(depth+1, valuelist + [s[:i] + 'Q' + s[i+1:]])  # 深度优先搜索

        # 关键技巧在于棋盘表示法，用一维数组即可表示，第0个Queen在board[0]列
        board = [-1 for i in xrange(n)]
        res = []
        dfs(0, [])
        return res


if __name__ == '__main__':
    s = Solution()
    print s.solveNQueens(4)

##########################################################################################
# 首先用一维数组记录每个Queen所处的列，这个表示方法很关键。然后对于每一个Queen判断每一列
# 是否冲突，如果不和之前的Queens冲突，则将Queen放至该列；否则剪枝。采用深度优先搜索找出所
# 有可能的解。
#