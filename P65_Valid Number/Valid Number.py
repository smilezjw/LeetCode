# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def isNumber(self, s):
        # 6种输入
        INVALID = 0   # 无效输入
        SPACE = 1     # 空格
        SIGN = 2      # 正负号 + -
        DIGIT = 3     # 数字
        DOT = 4       # 小数点
        EXPONENT = 5  # 指数e E
        # 状态转移表，行表示9种状态，列表示6种输入，
        # transitionTable[0][2]=3表示第0种状态，在输入第2种输入后跳转到第3种状态
        transitionTable = [[-1,  0,  3,  1,  2, -1],
                           [-1,  8, -1,  1,  4,  5],
                           [-1, -1, -1,  4, -1, -1],
                           [-1, -1, -1,  1,  2, -1],
                           [-1,  8, -1,  4, -1,  5],
                           [-1, -1,  6,  7, -1, -1],
                           [-1, -1, -1,  7, -1, -1],
                           [-1,  8, -1,  7, -1, -1],
                           [-1,  8, -1, -1, -1, -1]]
        # 初始状态为0
        state = 0
        i = 0
        while i < len(s):
            inputType = INVALID
            if s[i] == ' ':
                inputType = SPACE
            elif s[i] == '-' or s[i] == '+':
                inputType = SIGN
            elif s[i] in '0123456789':
                inputType = DIGIT
            elif s[i] == '.':
                inputType = DOT
            elif s[i] == 'e' or s[i] == 'E':
                inputType = EXPONENT
            # 进行状态转移
            state = transitionTable[state][inputType]
            # 如果输入后跳转的状态为无效状态，则直接返回False
            if state == -1:
                return False
            i += 1
        # 判断为数字的状态只有1或4或7或8
        return state == 1 or state == 4 or state == 7 or state == 8

if __name__ == '__main__':
    s = Solution()
    print s.isNumber('0')

############################################################################################
# 这道题用有穷自动机求解，难点在于状态的分割，要把每种情况都想到，还是很难理解的。分割9种
# 状态，其中只有1、4、7、8四种状态符合数字的要求。
# 具体参考：http://www.cnblogs.com/zuoyuan/p/3703075.html
#
