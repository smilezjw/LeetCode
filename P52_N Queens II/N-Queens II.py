# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def totalNQueens(self,n):
        def check(k, j):
            for i in xrange(k):
                if j == board[i] or abs(k - i) == abs(board[i] - j):
                    return False
            return True

        def dfs(depth):
            if depth == n:
                self.count += 1  # 这里只要记录解的个数就可以了
                return
            for i in xrange(n):
                if check(depth, i):
                    board[depth] = i
                    dfs(depth + 1)  # 这里不用表示出解的形式

        board = [-1 for i in xrange(n)]
        self.count = 0
        dfs(0)
        return self.count

if __name__ == '__main__':
    s = Solution()
    print s.totalNQueens(4)
    print s.totalNQueens(8)

##########################################################################################
# 这道题和上道题几乎是一样的做法，采用深度优先遍历，而且不用表示解的形式，只要记录解的个数
# 即可。
#