# coding=utf-8

"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

"""


class Solution(object):
    def singleNumber(self, A):
        A.sort()
        for i in range(0, len(A) - 1, 2):
            if A[i] != A[i + 1]:
                return A[i]
        return A[-1]


if __name__ == '__main__':
    a = Solution()
    print a.singleNumber([6, 3, 2, 2, 9, 3, 9])
