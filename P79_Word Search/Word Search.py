# coding=utf8

__author__ = 'smilezjw'

import copy

class Solution:
    def dfs(self, i, j, word):
        if len(word) == 0:
            return True
        # 向上查找邻接元素
        if i > 0 and Solution.board[i-1][j] == word[0]:
            tmp = Solution.board[i][j]
            Solution.board[i][j] = '#'
            if self.dfs(i-1, j, word[1:]):
                return True
            Solution.board[i][j] = tmp
        # 向下查找邻接元素
        if i < len(Solution.board) - 1 and Solution.board[i+1][j] == word[0]:
            tmp = Solution.board[i][j]
            Solution.board[i][j] = '#'
            if self.dfs(i+1, j, word[1:]):
                return True
            Solution.board[i][j] = tmp
        # 向左查找邻接元素
        if j > 0 and Solution.board[i][j-1] == word[0]:
            tmp = Solution.board[i][j]
            Solution.board[i][j] = '#'
            if self.dfs(i, j-1, word[1:]):
                return True
            Solution.board[i][j] = tmp
        # 向右查找邻接元素
        if j < len(Solution.board[0]) - 1 and Solution.board[i][j+1] == word[0]:
            tmp = Solution.board[i][j]
            Solution.board[i][j] = '#'
            if self.dfs(i, j+1, word[1:]):
                return True
            Solution.board[i][j] = tmp
        return False

    def exist(self, board, word):
        Solution.board = board
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == word[0]:  # 首先找到word中第一个元素
                    if self.dfs(i, j, word[1:]):
                        return True
        return False

if __name__ == '__main__':
    s = Solution()
    board = ['ABCE',
             'SFCS',
             'ADEE']
    currBoard = []
    for string in board:
        curr = list(string)
        currBoard.append(curr)
    currBoard2 = copy.deepcopy(currBoard)
    print s.exist(currBoard, 'ABCCED')
    print s.exist(currBoard2, 'SEE')
    print s.exist(currBoard, 'ABCB')

##############################################################################################
# 这道题用DFS来做，首先遍历二维数组找到word中的第0个元素，然后开始深度优先搜索，注意传入参数为
# 此时已经匹配到的位置i和j，然后从上下左右四个方向判断是否邻接元素也匹配。
# 如果匹配的话，则将遍历的元素用‘#’标志避免重复匹配；如果当前位置不匹配的话则还是原值，否则可
# 能其他情况可以匹配到的。
#