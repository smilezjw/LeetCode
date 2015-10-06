# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def wordPattern(self, pattern, str):
        str = str.split()
        if len(pattern) != len(str):
            return False
        hashTable = {}
        for i in xrange(len(pattern)):
            if pattern[i] not in hashTable:
                hashTable[pattern[i]] = str[i]
            if str[i] not in hashTable:
                hashTable[str[i]] = pattern[i]
            if hashTable[str[i]] != pattern[i] or hashTable[pattern[i]] != str[i]:
                return False
        return True

    def wordPattern_Solution2(self, pattern, str):
        s = str.split()
        p = pattern
        # list.index和string.find的作用是一样的，都是返回元素第一次出现的位置
        # map(s.index, s)返回一个list，每个元素第一次出现的位置
        # map(p.find, p)同样返回一个list，每个元素第一次出现的位置
        return map(s.index, s) == map(p.find, p)


if __name__ == '__main__':
    s = Solution()
    print s.wordPattern_Solution2('abba', 'dog cat cat dog')
    print s.wordPattern_Solution2('abba', 'dog cat cat fish')
    print s.wordPattern_Solution2('aaaa', 'dog cat cat dog')
    print s.wordPattern_Solution2('abba', 'dog dog dog dog')