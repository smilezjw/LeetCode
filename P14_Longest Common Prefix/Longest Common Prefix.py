# coding=utf8

__author__ = 'smilezjw'


def longestCommonPrefix(strs):
    if strs == []:         # 如果集合为空，则公共子前缀也为空
        return ''
    elif len(strs) == 1:   # 如果集合仅含有一个字符串，则公共子前缀就是该字符串
        return strs[0]
    else:
        prefix = strs[0]
        # 遍历一遍集合， 两两逐个进行比较，其实最长的公共子前缀由strs[0]决定了，后面不会超过这个长度
        for string in strs[1:]:
            prefixlen = len(prefix)
            strlen = len(string)
            # 如果公共子前缀的长度小于下一个字符串长度，比较string[:prefixlen]和prefix是否相等，
            # prefix已经是前面字符串的最长公共子前缀
            if prefixlen <= strlen and string[:prefixlen] != prefix:
                i = 0
                while i < prefixlen and prefix[i] == string[i]:
                    i += 1
                prefix = prefix[:i]
            # 如果公共子前缀长度大于下一个字符串长度，则重新匹配得到最长的公共子前缀长度
            elif strlen < prefixlen:
                i = 0
                while i < strlen and prefix[i] == string[i]:
                    i += 1
                prefix = string[:i]
        return prefix


if __name__ == '__main__':
    print longestCommonPrefix([])
    print longestCommonPrefix(['aa','a'])
    print longestCommonPrefix(['aa','aa','aabc'])
    print longestCommonPrefix(["","b"])
    print longestCommonPrefix(["c","c"])

##########################################################################################
# 这道题题目意思没有表达很明确，是要求集合中每个字符串的最长公共前缀，
# 也就是说每个字符串都必须包含这个最长公共前缀。
# 单遍扫描集合，两两逐个比较，最长公共前缀长度不超过strs[0]的长度。