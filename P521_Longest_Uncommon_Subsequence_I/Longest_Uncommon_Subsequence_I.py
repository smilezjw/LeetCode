# coding=utf8

class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        # 最长不公共子序列：两个字符串中任意一个字符串的子序列，不是另一个字符串的子序列，并且该子序列长度最长
        # 如果两个字符串相等，则没有不公共子序列；
        # 否则这两个字符串本身就是不公共子序列，选择长度较长的那个字符串即可
        return -1 if a == b else max(len(a), len(b))

if __name__ == '__main__':
    solution = Solution()
    print solution.findLUSlength('aba', 'cdc')
