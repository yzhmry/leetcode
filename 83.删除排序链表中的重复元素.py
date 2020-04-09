#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (48.89%)
# Likes:    273
# Dislikes: 0
# Total Accepted:    81.9K
# Total Submissions: 165.4K
# Testcase Example:  '[1,1,2]'
#
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
# 
# 示例 1:
# 
# 输入: 1->1->2
# 输出: 1->2
# 
# 
# 示例 2:
# 
# 输入: 1->1->2->3->3
# 输出: 1->2->3
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        #此为不带头结点的链表
        if head is None:  # 链表为空
            return head
        cur = head
        while cur.next:  # 下一节点不为空
            if cur.val == cur.next.val:  # 判断与下一节点的值是否相等
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

# @lc code=end

