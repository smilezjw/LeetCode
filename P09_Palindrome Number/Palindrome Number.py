# coding=utf8

__author__ = 'smilezjw'

def isPalindrome(x):
    if x < 0:
        return False
    elif 0 <= x < 10:
        return True
    else:
        flag = True
        num = x
        length = 0
        while x >= 10:
            x = x / 10
            length += 1
        ll = length
        while length > 0:
            if num / (10 ** length) != num % 10:
                flag = False
                break
            num = (num - (num / 10 ** length) * (10 ** length) - (num % 10))/10
            length -= 2
        return flag


if __name__ == '__main__':
    print isPalindrome(10021)
    print isPalindrome(121)
    print isPalindrome(-1)
    print isPalindrome(-1012147447412)

####################################################################################
# 如果将int转换为字符串，则需要extra space；
# 如果将整数反过来写，则会跟第7题一样出现溢出的问题；
# 因此这道题考虑从整数的第一个数字和最后一个数字比较，依次比较，
# 直到出现不相同的数字或者比较完成。
#