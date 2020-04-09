#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#
# https://leetcode-cn.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (43.73%)
# Likes:    357
# Dislikes: 0
# Total Accepted:    66K
# Total Submissions: 147.8K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# 删除链表中等于给定值 val 的所有节点。
# 
# 示例:
# 
# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        pre=ListNode(None)
        pre.next=head
        p=pre
        while p.next:
            if p.next.val==val:
                p.next=p.next.next
            else:
                p=p.next
        return pre.next
# @lc code=end

