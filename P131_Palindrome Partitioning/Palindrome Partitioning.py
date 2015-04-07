# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def partition(self, s):
        Solution.res = []
        self.partitionStr(s, [])
        return Solution.res

    def partitionStr(self, s, valueList):  # 分割字符串
        if len(s) == 0:
            Solution.res.append(valueList)
        # 遍历分割点，判断从该点分割出来的两段字符串是否都是回文字符串
        for i in xrange(1, len(s)+1):
            if self.isPalindrome(s[:i]):
                self.partitionStr(s[i:], valueList + [s[:i]])

    def isPalindrome(self, s):  # 判断是否为回文字符串
        for i in xrange(len(s)):
            if s[i] != s[-(i+1)]:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    print s.partition('cdd')
    print s.partition('bb')
    print s.partition('aab')

######################################################################################
# 深度递归，这道题我主要的问题在于：要遍历分割点，判断分割点前后的字符串是否都是回文
# 字符串。
#