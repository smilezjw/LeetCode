# coding=utf8

__author__ = 'smilezjw'


class Solution:
    # def isInterleave(self, s1, s2, s3):  # Time Limit Exceeded
    #     if s1 == s2 == s3 == '':
    #         return True
    #     if s1 != '' and s2 != '' and s3 != '' and s1[0] == s2[0] == s3[0]:
    #         if self.isInterleave(s1[1:], s2, s3[1:]) or self.isInterleave(s1, s2[1:], s3[1:]):
    #             return True
    #     elif s1 != '' and s3 != '' and s1[0] == s3[0]:
    #         if self.isInterleave(s1[1:], s2, s3[1:]):
    #             return True
    #     elif s2 != '' and s3 != '' and s2[0] == s3[0]:
    #         if self.isInterleave(s1, s2[1:], s3[1:]):
    #             return True
    #     return False

    def isInterleave(self, s1, s2, s3):
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)
        if len1 + len2 != len3:
            return False
        dp = [[False for i in xrange(len2+1)] for i in xrange(len1+1)]
        dp[0][0] = True
        for i in xrange(1, len1+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in xrange(1, len2+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        for i in xrange(1, len1+1):
            for j in xrange(1, len2+1):
                dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1] or dp[i][j-1] and s2[j-1] == s3[i+j-1]
        return dp[len1][len2]

if __name__ == '__main__':
    s = Solution()
    print s.isInterleave('def', '', 'de')
    print s.isInterleave('aabcc', 'dbbca', 'aadbbcbcac')
    print s.isInterleave('aabcc', 'dbbca', 'aadbbbaccc')
