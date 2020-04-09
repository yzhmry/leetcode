#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (59.36%)
# Likes:    844
# Dislikes: 0
# Total Accepted:    179.4K
# Total Submissions: 301.2K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 示例：
# 
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:


# 融合两个有序链表，首先定义一个临时结点pre，其后连接融合结果。
# 然后遍历两个链表，获得当前的结点l1和l2，结果链表后连接这两个结点中较小的结点，
# 并把该结点后移一位重新比较，直到其中一个链表已经遍历结束，
# 再把另一个链表的剩余部分挂在到当前结果上，返回临时结点pre后挂的结果链表即可。
        # 处理特殊情况
        if not l1:
            return l2
        if not l2:
            return l1

        pre = ListNode(0)          # 定义一个临时结点，用于挂载结果
        cur = pre                  # 定义当前结点

        while l1 and l2:                # 如果两个链表当前位置均不为空
            if l1.val < l2.val:         # 判断两个结点的大小
                cur.next = l1           # 将数值较小的结点挂载当前结点后面
                l1 = l1.next            # 数值较小的结点后移
            else:
                cur.next = l2
                l2 = l2.next

            cur = cur.next              # 后移当前结点

        cur.next = l1 or l2
        return pre.next            # 返回融合后的链表

# @lc code=end

