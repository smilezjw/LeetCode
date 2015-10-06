# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def gameOfLife(self, board):
        m = len(board)
        n = len(board[0])
        # 空间复杂度O(mn)，status用于标记下个时刻各个位置是否会改变状态
        status = [[0 for i in xrange(n)] for i in xrange(m)]
        dx = (1, 1, 1, 0, 0, -1, -1, -1)  # 8个方位便于计算
        dy = (1, 0, -1, 1, -1, 1, 0, -1)
        for i in xrange(m):
            for j in xrange(n):
                lives = 0
                for s in xrange(8):
                    nx = i + dx[s]
                    ny = j + dy[s]
                    if 0 <= nx < m and 0 <= ny < n:
                        lives += board[nx][ny]
                if (board[i][j] == 1 and (lives < 2 or lives > 3)) or (board[i][j] == 0 and lives == 3):
                    status[i][j] = 1
        for i in xrange(m):
            for j in xrange(n):
                if status[i][j] == 1:
                    board[i][j] ^= 1  # 0^1=1, 1^1=0
        return board

    def gameOfLife_Solution2(self, board):
        m = len(board)
        n = len(board[0])
        dx = (1, 1, 1, 0, 0, -1, -1, -1)
        dy = (1, 0, -1, 1, -1, 1, 0, -1)
        for x in xrange(m):
            for y in xrange(n):
                lives = 0
                for z in xrange(8):
                    nx = x + dx[z]
                    ny = y + dy[z]
                    lives += self.getCellStatus(board, nx, ny)
                # 如果初始状态为1，并且lives为2或3，则下一时刻保持1不变，因此1 | 10 = 11， 再右移一位还是1
                # 如果初始状态为0，并且lives为3，则下一时刻为1， 因此 0 | 10 = 10， 再右移一位变为1
                # 其他情况都是0，所以无论初始状态为0还是1，直接右移一位，都是由其高位的0填补过来的
                if lives + board[x][y] == 3 or lives == 3:
                    board[x][y] |= 2
        for x in xrange(m):
            for y in xrange(n):
                board[x][y] >>= 1

    def getCellStatus(self, board, x, y):
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
            return 0
        return board[x][y] & 1  # 和1位与，只返回最后一位数字表示其初始的状态


if __name__ == '__main__':
    s = Solution()
    board0 = [[0]]
    print s.gameOfLife(board0)

    board1 = [[1, 1], [1,0]]
    print s.gameOfLife(board1)
