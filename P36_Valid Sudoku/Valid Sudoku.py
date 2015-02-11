# coding=utf8

__author__ = 'smilezjw'


def isValidSudoku(board):
    hashBoard = {}
    for i in xrange(len(board)):
        for j in xrange(len(board[0])):
            if board[i][j] == '.':
                continue
            else:
                if board[i][j] not in hashBoard:  # 用hash表记录各个数字的位置
                    hashBoard[board[i][j]] = [[i, j]]
                else:
                    for p, q in hashBoard[board[i][j]]:
                        # 两个相同的数字不在同一个小的九宫格内，并且不在同一行内， 并且不在同一列内
                        if (abs(i - p) <= 2 and abs(j - q) <= 2 and i / 3 == p / 3 and j / 3 == q / 3) or i == p or j == q:
                            return False
                    hashBoard[board[i][j]].append([i, j])
    return True

if __name__ == '__main__':
    board = [".87654321",
             "2........",
             "3........",
             "4........",
             "5........",
             "6........",
             "7........",
             "8........",
             "9........"]
    board2 = ["..5.....6",
              "....14...",
              ".........",
              ".....92..",
              "5....2...",
              ".......3.",
              "...54....",
              "3.....42.",
              "...27.6.."]
    print isValidSudoku(board2)

################################################################################################
# 九宫格是否存在有效解的规则参考：http://sudoku.com.au/TheRules.aspx
# 判断给出的二维数组是否为有效的九宫格：
# 1.相同的数字不在同一行
# 2.相同的数字不在同一列
# 3.相同的数字不在同一个小的九宫格内，注意小的九宫格是固定的，
#   其判断条件为(abs(i - p) <= 2 and abs(j - q) <= 2 and i / 3 == p / 3 and j / 3 == q / 3)
#