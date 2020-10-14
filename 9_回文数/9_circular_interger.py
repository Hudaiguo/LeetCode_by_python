# -*- coding: utf-8 -*-
"""
@Time: 2020/10/14 23:54 
@Author: Hudaiguo
@python version: 3.5.2
#判断是否是回文数
#121 -> True
#-121 -> False
#72ms 13.5M
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:

        x = str(x)
        return(True if x==x[::-1] else False)
