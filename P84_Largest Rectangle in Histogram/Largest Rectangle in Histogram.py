# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def largestRectangleArea(self, height):
        i = 0
        stack = []
        area = 0
        while i < len(height):
            # 如果栈为空，或者当前高度比栈顶指向的高度更高，则将当前高度的索引入栈，表示可能的长方形的起点
            if stack == [] or height[i] > height[stack[-1]]:
                stack.append(i)
            # 如果栈不空，并且当前高度小于等于栈顶指向的高度
            # 那么弹出栈顶的元素，栈中的元素指向的高度肯定是递增的，不然不会入栈
            else:
                curr = stack.pop()
                # 既然栈中元素指向的高度是递增的，那么在计算区域面积时，高度就是栈顶弹出的元素指向的高度
                # 宽度则是i-1的位置减去现在栈顶的索引位置，因为i没有入栈
                # 如果高度连续递增，那么i-1-stack[-1] == 1；否则中间肯定有更高的高度之前已经出栈，所以高度可以用现在出栈的高度计算
                if stack == []:
                    width = i
                else:
                    width = i - 1 - stack[-1]
                area = max(area, width * height[curr])
                i -= 1
            i += 1
        # 同样的，如果列表遍历完了，但是栈不为空，则栈中索引指向的高度是递增的，此时i指向len(height)
        while stack != []:
            curr = stack.pop()
            if stack == []:
                width = i  # 此时i == len(height)
            else:
                width = i - 1 - stack[-1]
            area = max(area, width * height[curr])
        return area

if __name__ == '__main__':
    s = Solution()
    print s.largestRectangleArea([2, 1, 5, 6, 2, 3])
    print s.largestRectangleArea([1, 1, 3, 2, 2])

##########################################################################################
# 这道题比较复杂，需要画图理解。
# 1.如果栈为空，或者当前高度大于栈顶指向的高度，则将当前高度入栈；
# 2.如果栈不空并且当前高度小于等于栈顶指向的高度，则将栈顶指向的高度出栈并用来计算矩阵的
# 高度，宽度=i-1-出栈后栈顶的索引，计算得到区域面积。
# 3.如果列表遍历完后，栈不为空，则逐个出栈，宽度为列表长度len(A) - 1 - 出栈后栈顶的索引，
# 计算区域面积。
# 需要注意：栈中索引指向的高度肯定是递增的。因此如果连续递增，那么宽度为1；否则，中间肯定是有一个
# 更高的高度之前已经出栈，因此宽度>1。
#