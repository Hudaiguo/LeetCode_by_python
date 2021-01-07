# -*- coding: utf-8 -*-
"""
@Time:   2021/1/7 15:20
@Author: Hudaiguo
@python version: 3.5.2
"""

"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
你可以按任意顺序返回答案。

执行用时：40 ms , 在所有 Python3 提交中击败了 77.06%的用户
内存消耗：14.9 MB , 在所有 Python3 提交中击败了20.86%的用户
"""

class Solution:
    def twoSum(self, nums, target):
        for index, num in enumerate(nums):
            for index_2, num_2 in enumerate(nums[index+1:]):
                if target == num + num_2:
                    return [index, index_2+index+1]


test = Solution()
print(test.twoSum([2, 7, 11, 15], 9))