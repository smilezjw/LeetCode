# coding=utf8

__author__ = 'smilezjw'


def isValid(s):
    stack = []  # python中可以用list来用作栈
    for n in s:
        stack.append(n)
        if len(stack) >= 2:
            temp = stack[len(stack) - 2] + stack[len(stack) - 1]  #判断最后两个字符是否匹配
            if temp in ['()', '[]', '{}']:                       #最后两个字符匹配则弹出
                stack.pop()
                stack.pop()
    if len(stack) > 0:
        return False
    else:
        return True

if __name__ == '__main__':
    print isValid('()')
    print isValid('{[()]}')
    print isValid('([)]')

####################################################################################
# 这道题用栈的思想，先进后出，每次进入一个字符，判断栈顶的两个字符是否匹配；
# 如果匹配则弹出，否则继续进入字符。
# 最后如果全部匹配弹出则栈中为空，否则不为空。