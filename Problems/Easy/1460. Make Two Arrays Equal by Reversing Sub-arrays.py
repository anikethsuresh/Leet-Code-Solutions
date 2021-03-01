"""

1460. Make Two Arrays Equal by Reversing Sub-arrays
There are two things we can check here.

1. If the elements in both the sets are the same.
2. The sorted list contains elements in the same order.

Check these two conditions and we have our required result.
"""

class Solution:
    def canBeEqual(self, target, arr):
        target.sort()
        arr.sort()
        for index in range(len(target)):
            if target[index] != arr[index]:
                return False
        return True
        

runThis = Solution()
final_results = runThis.canBeEqual([1,2,3,4], [2,4,1,3])
print(final_results) 