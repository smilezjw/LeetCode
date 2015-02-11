# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def longestValidParentheses(self, s):
        stack = [(-1, ')')]  # 使用栈
        maxLen = 0
        for i in xrange(len(s)):
            if s[i] == ')' and stack[-1][1] == '(':  # 匹配‘()’
                stack.pop()
                # 先出栈，然后求当前索引减去栈顶元素的索引，主要是这一步
                maxLen = max(maxLen, i - stack[-1][0])
            else:
                stack.append((i, s[i]))
        return maxLen

if __name__ == '__main__':
    sol = Solution()
    print sol.longestValidParentheses('(()')
    print sol.longestValidParentheses(')()())')
    print sol.longestValidParentheses('()(()')
    print sol.longestValidParentheses('()(())')

################################################################################################
# 这道题用栈的方法，将遇到的左括号都入栈，遇到右括号如果与左括号匹配则将该左括号出栈，并且更新
# 长度，这里长度计算将右括号的索引减去栈顶元素的索引。如果不匹配，则继续入栈。
# 这道题貌似还可以用动态规划做，还没有看明白 = =
#
