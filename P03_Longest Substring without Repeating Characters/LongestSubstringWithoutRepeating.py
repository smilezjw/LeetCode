# _*_ coding:utf8 _*_

__author__ = 'smilezjw'


def lengthOfLongestSubstring(s):
    substr = {}
    length = 0
    templen = 0
    start = 0
    for i, n in enumerate(s):
        if n not in substr.keys() or substr[n] < start: # 如果某个字符已经出现，但是是在上一个判断的子串中出现，则substr[n] < start
            substr[n] = i
            templen += 1  #对这个子串长度进行计数
            length = max(length, templen)
        else:
            templen = i - substr[n]  # 上一次出现与这一次中间隔了几个字符
            length = max(length, templen)
            start = substr[n] + 1    # 这一次的子串起始位置变为上一次出现重复字符的位置+1
            substr[n] = i            # 更新重复字符的位置
    return length

if __name__ == '__main__':
    print lengthOfLongestSubstring('aab')
    print lengthOfLongestSubstring('pwwkew')
    print lengthOfLongestSubstring('abcabcbb')
    print lengthOfLongestSubstring('bbbbb')
    print lengthOfLongestSubstring('')
    print lengthOfLongestSubstring('wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco')

######################################################################################
# 扫描字符串，当遇到已经出现过的字符时，认为已经出现最长不重复子串的可能，因此接下去从
# 上次出现的位置+1开始判断。巧妙的是不需要每次都从上次出现重复字符的位置开始重新扫描，
# 只需要计算两次出现的位置之间隔了几个字符（这些字符肯定是不相同的），并且更新hash表中
# 重复字符的位置。图示可以参考http://blog.csdn.net/likecool21/article/details/10858799。
#