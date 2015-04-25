# coding=utf8

__author__ = 'smilezjw'

class Solution:
    def findRepeatedDnaSequences(self, s):
        res = []
        hashtable = {}
        for i in xrange(len(s)-9):
            # 这里用了dict.get(key, 0)函数，如果key在dict中则返回key对应的value，否则返回0
            hashtable[s[i:i+10]] = hashtable.get(s[i:i+10], 0) + 1
            if hashtable[s[i:i+10]] == 2:
                res.append(s[i:i+10])
        return res

if __name__ == '__main__':
    s = Solution()
    print s.findRepeatedDnaSequences('AACC')
    print s.findRepeatedDnaSequences('AAAAAAAAAAA')
    print s.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')

########################################################################################
# 这道题遍历字符串，每次遍历将长度为10的字符串存入hash表中，然后取出出现多余一次的字符串。
#