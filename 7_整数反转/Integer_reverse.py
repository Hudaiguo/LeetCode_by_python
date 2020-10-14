# -*- coding: utf-8 -*-
"""
@Time: 2020/10/14 22:25 
@Author: Hudaiguo
@python version: 3.5.2
#整数反转
#-170 -> -71
#170 -> 71
#123 -> 321
#超过32位存储返回0
#44ms 13.6M -> 36ms 13.5M
"""

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        x = str(x)
        if x[0] == "-" or x[0] == "+":
            while x[-1] == "0":
                x = x[:-1]
            y = int(x[0] + x[1:][::-1])
        elif x[-1] != "0":
            y = int(x[::-1])
        else:
            while x[-1] == "0":
                x = x[:-1]
            y =  int(x[::-1])

        if -2**31-1 < y < 2**31:
            return y
        else:
            return 0

    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        x = str(x)
        while x[-1] == "0":
            x = x[:-1]
        if x[0] == "-":
            y = int(x[0] + x[1:][::-1])
        else:
            y =  int(x[::-1])

        if -2**31-1 < y < 2**31:
            return y
        else:
            return 0


Integer = Solution()
print(Integer.reverse2(1534236469))