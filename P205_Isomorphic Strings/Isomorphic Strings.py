# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def isIsomorphic(self, s, t):
        hashtable = {}
        for i in xrange(len(s)):
            # 如果s[i]已经在哈希表中了说明已经映射到t中的某个字符
            if s[i] in hashtable:
                # 但是现在s[i]又映射到t中另外一个字符，那么就返回False
                if hashtable[s[i]] != t[i]:
                    return False
            # 如果s[i]不在哈希表中
            # 首先判断s[i]对应的t[i]是否已经被映射过，因为规定是一一对应的关系
            elif t[i] in hashtable.values():
                return False
            # 如果s[i]不在哈希表中，并且t[i]也没有并映射过，那么将这一对添加到哈希表中
            else:
                hashtable[s[i]] = t[i]
        return True

if __name__ == '__main__':
    s = Solution()
    print s.isIsomorphic('', '')
    print s.isIsomorphic('ab', 'aa')
    print s.isIsomorphic('egg', 'add')
    print s.isIsomorphic('foo', 'bar')
    print s.isIsomorphic('paper', 'title')

#####################################################################################
# 这一题比较简单，主要是用哈希表存储s和t中字符一一映射关系，需要判断s和t是否存在一对
# 多或者多对一的关系。
#
