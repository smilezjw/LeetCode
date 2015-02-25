# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def check(self, k, j):
        for i in xrange(k):
            if j == self.board[i] or abs(k - i) == abs(self.board[i] - j):
                return False
        return True

    def totalNQueens(self, n):
        self.board = [-1 for i in xrange(n)]  # 初始化棋盘表示
        count = 0   #  记录解的个数
        row = 0     #  行号
        col = 0     #  列号
        while row < n:
            while col < n:
                if self.check(row, col):
                    self.board[row] = col
                    col = 0
                    break
                else:
                    col += 1
            if self.board[row] == -1:  # 如果Queen在该行找不到摆放的位置
                # 如果在第0行也找不到摆放的位置，说明所有情况迭代完毕，跳出循环
                if row == 0:
                    break
                else:    # 回溯到上一行
                    row -= 1
                    col = self.board[row] + 1  # Queen摆放的初始位置加1，尝试下一列
                    self.board[row] = -1       # 重新寻找该行可以摆放Queen的位置
                    continue
            if row == n-1:  # 当最后一行的Queen位置确定后，则得到一个解
                count += 1  # 解的个数加1
                col = self.board[row] + 1  # 然后重新尝试新的解，尝试下一列
                self.board[row] = -1       # 重新寻找该行Queen的位置
                continue
            row += 1
        return count

if __name__ == '__main__':
    s = Solution()
    print s.totalNQueens(4)
    print s.totalNQueens(8)

##########################################################################################
# 这道题除了用递归的方法，这里还用了非递归的方法，用循环来判断各个情况及递归的出口。
# 首先判断第row行的Queen在第col列的摆放位置是否可以，找到该行的摆放位置；如果该行没有合适的
# 摆放位置，则回溯到上一行，并且修改上一行Queen的摆放位置；如果已经回溯到第0行，则所有解都
# 已经遍历好了，因此直接跳出循环返回解的个数。当第n-1行Queen的位置也确定后，即得到一个解，然后
# 尝试该行下一个位置，得到其他解。
#