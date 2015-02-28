# coding=utf8

__author__ = 'smilezjw'


def nextPermutation(num):
    if len(num) <= 1:
        return num
    partition = -1
    for i in xrange(len(num)-2, -1, -1): # 从右到左找到第一个降序的元素标记为partition
        if num[i] < num[i+1]:
            partition = i
            break
    # 如果整个序列从右到左都是升序（也就是从左到右都是降序），那么直接反转列表即可，如3,2,1 -> 1,2,3
    if partition == -1:
        num.reverse()
        return num
    for i in xrange(len(num)-1, partition, -1):  # 然后从右到左找到第一个大于下标为partition的元素
        if num[i] > num[partition]:
            num[i], num[partition] = num[partition], num[i] # 将这两个元素呼唤
            break
    num[(partition+1):] = num[(partition+1):][::-1] # 最后对下标为partition之后的元素顺序反转
    return num

if __name__ == '__main__':
    print nextPermutation([1, 2, 3])
    print nextPermutation([1, 5, 1])
    print nextPermutation([3, 2, 1])

################################################################################################
# 啊呀，这种思路谁能想得到啊= = 附上人家的思路说明：
# http://fisherlei.blogspot.com/2012/12/leetcode-next-permutation.html
# 1.From right to left, find the first digit which violate the increase trend as the PartitionNumber.
# 2.From right to left, find the first digit which is greater than PartitionNumber, as the ChangeNumber.
# 3.Swap the PartitionNumber and the ChangeNumber.
# 4.Reverse all the digits on the right of partition index.