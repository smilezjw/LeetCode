# coding=utf8

__author__ = 'smilezjw'

def gen(num, s, leftParentNum, rightParentNum, res):
    if leftParentNum == rightParentNum == num:
        res.append(s)
        return res
    if leftParentNum < num:
        gen(num, s + '(', leftParentNum + 1, rightParentNum, res)
    if rightParentNum < leftParentNum:
        gen(num, s + ')', leftParentNum, rightParentNum + 1, res)

def generateParenthesis(n):
    # result = []
    # if n == 1:
    #     return ['()']
    # if n > 1:
    #     for i in generateParenthesis(n-1):
    #         if '(' + i + ')' not in result:
    #             result.append('(' + i + ')')
    #         if  '()' + i not in result:
    #             result.append( '()' + i)
    #         if i + '()' not in result:
    #             result.append(i + '()')
    #     return result

    res = []
    gen(n, '', 0, 0, res)
    result = res
    return result

if __name__ == '__main__':
    print generateParenthesis(2)
    print generateParenthesis(3)
    print generateParenthesis(4)

##########################################################################################
# 这道题一开始按照自己的思路（注释掉的部分）确实存在有些情况没有考虑到，虽然想到了要用
# 递归的思路去解题，但是思路不正确。
# 看了网上参考的解答，用到了宽度优先搜索BFS，果然又拓宽了思路啊。
# 如果左括号数量小于n，增加左括号；如果右括号数量小于左括号数量，增加右括号；
# 如果左括号数量 ==  右括号数量 == n，则得到一个解。