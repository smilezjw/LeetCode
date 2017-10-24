# coding=utf8

class Solution(object):
    def reverseWords(self, s):
        # return " ".join(s[::-1].split(" ")[::-1])
        return " ".join(s.split(" ")[::-1])[::-1]    # a little faster than the first solution

if __name__ == '__main__':
    solution = Solution()
    print solution.reverseWords("Let's take LeetCode contest")
