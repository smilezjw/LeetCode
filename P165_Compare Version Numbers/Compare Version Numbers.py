# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def compareVersion(self, version1, version2):
        if version1 == '' or version2 == '':
            return 0
        ver1 = version1.split('.')
        ver2 = version2.split('.')
        # 如果两个版本字符的长度不一致，则较短的字符串后面补0
        distance = abs(len(ver1) - len(ver2))
        if len(ver1) > len(ver2):
            ver2 += [0] * distance
        elif len(ver2) > len(ver1):
            ver1 += [0] * distance
        # 从前往后比较，将字符转化为整数类型，避免类似于01和1比较的情况
        for i in xrange(len(ver1)):
            if int(ver1[i]) > int(ver2[i]):
                return 1
            elif int(ver1[i]) < int(ver2[i]):
                return -1
        return 0

if __name__ == '__main__':
    s = Solution()
    print s.compareVersion('0.1', '1.1')
    print s.compareVersion('1', '1.1')
    print s.compareVersion('01', '1')
    print s.compareVersion('10.6.5', '10.6')

######################################################################################
# 这道题比较简单，但也有以下几点需要注意：
# 1.两个版本字符串长度不一致，较短的字符串需要补0；
# 2.在逐位比较时需要转化为整数来比较，避免'01'和'0'不一致的情况。
#