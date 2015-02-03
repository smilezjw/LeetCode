# coding=utf-8

__author__ = 'smilezjw'


def convert(s, nRows):
    ss = ''
    #横着排列和竖着排列情况是一样一样的
    if len(s) <= nRows or nRows <= 1:
        return s
    else:
        # 分组，|/形状的字符串为一组，每组个数最多为 2 * nRows - 2
        groups = (len(s) / (2*nRows - 2)) + 1
        for j in xrange(nRows):
            for i in xrange(groups):
                # i * (2 * nRows - 2) + j 为|的字符串的位置索引
                # i * (2 * nRows - 2) + 2 * nRows - j - 2 为/的字符串的位置索引
                # (2 * nRows - j - 2) % (2 * nRows - 2) == 0 判断是否是|第一个字符
                # j == (2 * nRows - j - 2) 判断是否是|最后一个字符
                # 这两种情况直接把这个字符添加到字符串中即可， 否则要添加两个字符
                if i*(2 * nRows - 2)+j < len(s) and (i*(2*nRows-2) + 2*nRows - j - 2) < len(s):
                    if j == (2 * nRows - j - 2) or ((2 * nRows - j - 2) % (2*nRows-2) == 0):
                        ss += s[i*(2 * nRows - 2)+j]
                    else:
                        ss = ss + s[i*(2*nRows-2) + j] + s[i*(2*nRows-2) + 2*nRows - j - 2]
                elif i*(2 * nRows - 2)+j < len(s):
                    ss += s[i*(2 * nRows - 2)+j]
        return ss

if __name__ == '__main__':
    print convert('apple', 3)
    print convert('', 1)
    print convert('A', 1)
    print convert('AB', 1)

###########################################################################################
# 感觉这道题首先需要搞清楚题目意思，zigzag pattern到底是怎么样排列的， 是|/|/|类似于这样的。
# 然后找出字符串索引位置的规律，我使用2个变量，i表示分组，j表示每组中的行号，找出二维变量与
# 最后排列情况之间的规律。
# 需要注意特殊情况，即横着排列和竖着排列是一样的情况。
