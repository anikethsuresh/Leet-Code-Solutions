"""

303. Range Sum Query - Immutable

This is an incredibly simple solution.
It is possible to optimize this solution for the following cases:

1. If the user might call sumRange with the same arguments, we might want to cache the results to prevent the added overhead
2. We might want to precompute all the possible calls to this function, so that the call to sumRange would be O(1)
"""


class NumArray:

    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, i, j):
        count = 0
        for index in range(i , j+1):
            count += self.nums(index)
        return count


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)