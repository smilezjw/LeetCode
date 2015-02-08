# coding=utf8

__author__ = 'smilezjw'


def strStr(haystack, needle):
    if haystack == needle == '':
        return 0
    length = len(needle)
    for i in xrange(len(haystack)):
        if haystack[i: i+length] == needle:
            return i
    return -1

if __name__ == '__main__':
    print strStr('aabbaa','bb')
    print strStr('','')

################################################################################################
# 这道题自己做么直接就brute force method暴力搜索了，竟然leetcode直接就accept了，好意外，还以为
# 大数据集会过不去呢= = 原来这道题的本意就是可以用暴力搜索的，O(mn)时间复杂度，O(1)空间复杂度。
# 不过对于面试官而言，可能更加希望看到Rabin-Karp algorithm, KMP algorithm
# 和 the Boyer- Moore algorithm，待研究！
#
