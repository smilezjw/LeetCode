# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def lengthOfLastWord(self, s):
        #words = s.split(' ')  # words==['b', '', '', 'a', '', '', '', '']
        words = s.split()  # words == ['b', 'a']
        return len(words[-1]) if words != [] else 0

if __name__ == '__main__':
    s = Solution()
    print s.lengthOfLastWord('a')
    print s.lengthOfLastWord('Hello World')
    print s.lengthOfLastWord('b   a    ')

#########################################################################################
# 这道题主要靠python字符串处理能力split，要注意split()和split(' ')是的区别：
# If sep is not specified or is None, a different splitting algorithm is applied: runs
# of consecutive whitespace are regarded as a single separator, and the result will
# contain no empty strings at the start or end if the string has leading or trailing
# whitespace. Consequently, splitting an empty string or a string consisting of just
# whitespace with a None separator returns [].