# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def solveSudoku(self, board):
        self.dfs(board)
        return board

    def isValid(self, p, q, board):  #判断board[p][q]位置上的数字是否有效
        temp = board[p][q]
        board[p] = board[p][:q] + 'D' + board[p][q+1:]
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] == temp and ((abs(i - p) <= 2 and abs(j - q) <= 2 and i / 3 == p / 3 and j / 3 == q / 3) or i == p or j == q):
                    return False
        board[p] = board[p][:q] + temp + board[p][q+1:]
        return True

    def dfs(self, board):
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] == '.':
                    for k in '123456789':
                        # 字符串是不可变类型，要改变ij位置上的值只能这么写
                        board[i] = board[i][:j] + k + board[i][j+1:]
                        if self.isValid(i, j, board) and self.dfs(board):
                            return True
                        board[i] = board[i][:j] + '.' + board[i][j+1:]
                    return False
        return True

if __name__ == '__main__':
    board = ["..9748...",
             "7........",
             ".2.1.9...",
             "..7...24.",
             ".64.1.59.",
             ".98...3..",
             "...8.3.2.",
             "........6",
             "...2759.."]
    s = Solution()
    print s.solveSudoku(board)

#################################################################################################
# 深度优先搜索，每填写一个数字，都要判断该数字填写在该位置上是否正确。
# 这里需要注意字符串是不可变类型，如果直接board[p][q] = k的话，会报错：
# 'str' object does not support item assignment
# 因此需要用分片赋值的方法才能改变字符串。