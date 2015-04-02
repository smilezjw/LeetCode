# coding=utf8
import collections

__author__ = 'smilezjw'


class Solution:
    # 这种做法一直报Runtime Error
    def solve(self, board):
        if len(board) > 1 and len(board[0]) > 1:
            Solution.board = board
            m = len(board) - 1
            n = len(board[0]) - 1
            Solution.visited = [[False for j in xrange(n+1)] for i in xrange(m+1)]
            for j in xrange(n+1):
                if Solution.board[0][j] == 'O':
                    self.edge(0, j)
                if Solution.board[m][j] == 'O':
                    self.edge(m, j)
            for i in xrange(m+1):
                if Solution.board[i][0] == 'O':
                    self.edge(i, 0)
                if Solution.board[i][n] == 'O':
                    self.edge(i, n)
            for i in xrange(m+1):
                for j in xrange(n+1):
                    if Solution.board[i][j] == 'O':
                        Solution.board[i] = Solution.board[i][:j] + 'X' + Solution.board[i][j+1:]
                    elif Solution.board[i][j] == '$':
                        Solution.board[i] = Solution.board[i][:j] + 'O' + Solution.board[i][j+1:]
            return board

    def edge(self, i, j):
        if Solution.board[i][j] == 'O':
            Solution.board[i] = Solution.board[i][:j] + '$' + Solution.board[i][j+1:]
            Solution.visited[i][j] = True
            if i < len(Solution.board) - 1 and not Solution.visited[i+1][j]:
                self.edge(i+1, j)
            if i > 0 and not Solution.visited[i-1][j]:
                self.edge(i-1, j)
            if j > 0 and not Solution.visited[i][j-1]:
                self.edge(i, j - 1)
            if j < len(Solution.board[0]) - 1 and not Solution.visited[i][j+1]:
                self.edge(i, j + 1)


    def solveBoard(self, board):  # 这种方法不需要递归，只要循环就可以解决
        if len(board) > 1 and len(board[0]) > 1:
            m = len(board)
            n = len(board[0])
            queue = []  # 记录不能被'X'包围住的'O'
            # 判断是否访问过，用于剪枝
            visited = [[False for j in xrange(n)] for i in xrange(m)]
            # 从外层四条边上的'O'入手，因为外层四条边上的'O'不会被'X'包围起来
            for j in xrange(n):
                # 第0行
                if board[0][j] == 'O':
                    queue.append((0, j))
                # 最后一行
                if board[m-1][j] == 'O':
                    queue.append((m-1, j))
            for i in xrange(m):
                # 第0列
                if board[i][0] == 'O':
                    queue.append((i, 0))
                # 最后一列
                if board[i][n-1] == 'O':
                    queue.append((i, n-1))
            while queue:
                curr = queue.pop(0)
                # 如果是不能被包围住的O，则用其他符号代替
                if board[curr[0]][curr[1]] == 'O':
                    board[curr[0]][curr[1]] = '$'
                visited[curr[0]][curr[1]] = True
                # 然后判断这个不能被X包围住的O的位置的上下左右位置是否也是O
                if curr[0] < m - 1 and board[curr[0] + 1][curr[1]] == 'O' and not visited[curr[0] + 1][curr[1]]:
                    queue.append((curr[0]+1, curr[1]))
                if curr[0] > 0 and board[curr[0] - 1][curr[1]] == 'O' and not visited[curr[0] - 1][curr[1]]:
                    queue.append((curr[0]-1, curr[1]))
                if curr[1] < n - 1 and board[curr[0]][curr[1] + 1] == 'O' and not visited[curr[0]][curr[1] + 1]:
                    queue.append((curr[0], curr[1]+1))
                if curr[1] > 0 and board[curr[0]][curr[1] - 1] == 'O' and not visited[curr[0]][curr[1] - 1]:
                    queue.append((curr[0], curr[1]-1))
            for i in xrange(m):
                for j in xrange(n):
                    if board[i][j] == 'O':
                        board[i][j] = 'X'
                    elif board[i][j] == '$':
                        board[i][j] = 'O'
            return board


if __name__ == '__main__':
    s = Solution()
    board = ['XXXX',
             'XOOX',
             'XXOX',
             'XOXX']
    board2 = ["XXX","XOX","XXX"]
    board3 = ['OO', 'OO']
    board4 = ["XOXOXO","OXOXOX","XOXOXO","OXOXOX"]
    print s.solveBoard(board3)

#########################################################################################
# 这道题自己用递归写就复杂度太高了，大数据集通不过。
# 参考人家的代码用循环解决，用列表记录从外层四条边开始不能被X包围住的O的位置，然后暂时用
# 其他符号代替，直至列表中所有不能被X包围的O的位置全部遍历完成。
# 主要还是考虑用循环解决的思路。