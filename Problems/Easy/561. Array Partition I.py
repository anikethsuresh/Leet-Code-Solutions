"""

561. Array Partition I
The subtelty of this question is brilliant.
To obtain the maximum value we need to sacrifice the smallest after a small number. If we do it the other way, we end up
sacrificing a large number for a small number, therfore by doing so we reduce the gap between the numbers, thus maximizing the sum

"""

class Solution:
    def arrayPairSum(self, nums: int):
        nums.sort()
        result = 0
        for i in range(0,len(nums),2):
            result += nums[i]
        return result

runThis = Solution()
final_results = runThis.arrayPairSum([6,2,6,5,1,2])
print(final_results) 