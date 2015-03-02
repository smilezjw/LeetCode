# coding=utf8

__author__ = 'smilezjw'


class Solution:
    # def simplifyPath(self, path):
    #     stack = []
    #     i = 0
    #     j = 0
    #     while i < len(path) - 1:
    #         if path[i] == '/' and path[i+1] != '.' and path[i+1] != '/':
    #             stack.append(path[i])
    #             j = len(stack) - 1
    #         elif path[i] == '.' and path[i+1] == '.':
    #             i += 1
    #             stack = stack[:j]
    #         elif path[i] != '/' and path[i] != '.':
    #             stack.append(path[i])
    #         i += 1
    #     if path[-1] != '.':
    #         if (len(path) > 1 and path[-2] != '.' and path[-2] != '/') or len(path) == 1:
    #             stack.append(path[-1])
    #     if stack == []:
    #         return '/'
    #     return ''.join(stack)

    def simplifyPath(self, path):
        stack = []  # 使用栈来存储达到的目录
        i = 0
        res = ''
        while i < len(path):
            end = i + 1
            while end < len(path) and path[end] != '/':  # 得到每两个/之间的路径
                end += 1
            sub = path[i+1:end]
            if len(sub) > 0:
                if sub == '..':  # '...'表示上级目录，则将当前路径出栈返回上级目录
                    if len(stack) > 0:
                        stack.pop()
                elif sub != '.':  # '.'表示当前目录，不做操作
                    stack.append(sub)
            i = end
        if stack == []:  # 如果路径为空，则表示在根目录下'/'
            return '/'
        for i in stack:  # 对于每个目录添加/表示简化的路径
            res += '/' + i
        return res

if __name__ == '__main__':
    s = Solution()
    print s.simplifyPath('///')
    print s.simplifyPath('/...')  # 请注意特殊情况，这个路径返回的还是'/...'
    print s.simplifyPath('/../a/b/c/./..')

###########################################################################################
# Unix '/'表示根目录，'.'表示当前目录，'..'表示上级目录。这道题用栈的数据结构来做。
# 首先要最长匹配两个/之间字符串，如果是'..'则返回上级目录，栈中弹出当前目录则返回上级目录；
# 如果是'.'则保留在当前目录，对栈不进行任何操作；
# 如果是其他字符串，则表示进入到该目录，将字符串入栈。
# 尤其需要注意不能混淆的是'/...'这种情况，最长匹配'...'该字符串表示一个文件，相当于'aaa'，而不
# 是先'..'然后'.',要满足最长匹配的原则。