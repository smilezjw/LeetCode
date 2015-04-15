# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def reverseWords(self, s):
        # words = s.strip().split()
        # if len(words) == 0:
        #     return ''
        # res = words[-1]
        # for i in xrange(len(words)-2, -1, -1):
        #     res += ' ' + words[i]
        # return res

        # 这种写法多么简洁
        return ' '.join(s.strip().split()[::-1])

if __name__ == '__main__':
    s = Solution()
    print s.reverseWords('the sky is blue')

########################################################################################
# 这道题体现python处理字符串的强大功能！代码简洁一行搞定。
#