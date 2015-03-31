# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def isPalindrome(self, s):  # 代码比较冗余
        string = []
        for i in xrange(len(s)):
            if s[i].isalnum():
                string.append(s[i].lower())
        length = len(string)
        if length <= 1:
            return True
        i = 0
        j = length - 1
        if length % 2 == 0:
            while i < j:
                if string[i] != string[j]:
                    return False
                else:
                    i += 1
                    j -= 1
        else:
            while i <= j:
                if string[i] != string[j]:
                    return False
                else:
                    i += 1
                    j -= 1
        return True

    def isPalindrome_Concise(self, s):  # 稍微简练一点
        if s == '':  # 注意空串也默认为是回文串
            return True
        stemp = ''
        for i in xrange(len(s)):
            if s[i].isalnum():  # 判断该字符是否是数字或者是字母
                stemp += s[i]
        stemp = stemp.lower()   # 忽略字母大小写
        for i in xrange(len(stemp)/2):  # 这样写的话可以不考虑是偶数长度还是奇数长度
            if stemp[i] != stemp[len(stemp) - 1 - i]:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    print s.isPalindrome_Concise('')
    print s.isPalindrome_Concise('A man, a plan, a canal: Panama')

#########################################################################################
# 这道题比较简单，主要考虑：
# 1.空串也默认是回文字符串；
# 2.注意要去除非数字或字母的字符；
# 3.忽略字母大小写。
#