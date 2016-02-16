# coding=utf8

import  collections

class Solution(object):
    def removeDuplicateLetters(self, s):
        # Counter统计字符串s中各个字符出现的次数
        counter = collections.Counter(s)
        stack = []
        for i in xrange(len(s)):
            counter[s[i]] -= 1
            if s[i] in stack:
                continue
            # 如果s[i]不在栈中，如果s[i]小于栈顶元素，并且栈顶元素在后续字符串中还会出现，则弹出栈顶元素
            while stack and s[i] < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()
            # 如果s[i]不在栈中，则将s[i]入栈
            stack.append(s[i])
        return ''.join(stack)


if __name__ == '__main__':
    s = Solution()
    print s.removeDuplicateLetters('cbacdcbc')

##########################################################################
# 这道题目的意思在于既要获取字符串的最小字典序，还要保持在原字符串中的相对顺序。
#
