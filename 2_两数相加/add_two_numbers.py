# -*- coding: utf-8 -*-
"""
@Time:   2021/1/7 15:50
@Author: Hudaiguo
@python version: 3.5.2
"""

"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
"""
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Node_handle():
    def __init__(self):
        self.cur_node = None
    def add(self,data):
        node = Node()
        node.val = data
        node.next = self.cur_node
        self.cur_node = node
        return node

class Solution:
    def addTwoNumbers(self, l1, l2):
        num1, num2 = '', ''
        while l1:
            # print ('\nnode: ', 'l1', ' value: ', l1.val, ' next: ', l1.next)
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            # print ('\nnode: ', 'l2', ' value: ', l2.val, ' next: ', l2.next)
            num2 += str(l2.val)
            l2 = l2.next
        num1, num2 = num1[::-1], num2[::-1]
        print(num1, num2)
        result = int(num1) + int(num2)
        print(result)
        l3 = Node()
        ListNode_1 = Node_handle()
        l3_list = [int(i) for i in str(result)][::-1]
        print(l3_list)
        for i in l3_list:
            l3 = ListNode_1.add(i)
        return l3





class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        re = ListNode(0)
        r = re
        carry = 0  #进位
        while(l1 or l2):
            x= l1.val if l1 else 0
            y= l2.val if l2 else 0
            s=carry+x+y
            carry=s//10
            r.next=ListNode(s%10)
            r=r.next
            if(l1!=None):l1=l1.next
            if(l2!=None):l2=l2.next
        if(carry>0):
            r.next=ListNode(1)
        return re.next

