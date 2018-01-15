# coding=utf8

class Solution(object):
    def detectCapitalUse(self, word):
        # if len(word) < 2:
        #     return True
        # return word.upper() == word or word[1:].lower() == word[1:]

        return word.isupper() or word.islower() or word.istitle()

if __name__ == '__main__':
    solution = Solution()
    word = 'Google'
    print(solution.detectCapitalUse(word))
