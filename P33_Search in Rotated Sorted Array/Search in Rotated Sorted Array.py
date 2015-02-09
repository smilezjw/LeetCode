# coding=utf8

__author__ = 'smilezjw'

# 哈哈，这么简单的方法直接accept了好么，只要43ms哦！大家为什么非要费劲脑细胞去想如何用二分查找呢，唉= =
def search(A, target):
    if target in A:
        return A.index(target)
    else:
        return -1

if __name__ == '__main__':
    print search([0,1,2,3,4,5,6], 6)
