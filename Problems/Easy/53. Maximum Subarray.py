"""

53. Maximum Subarray

This implementation follows Kadane's algorithm.

Notes:
1) We use dynamic programming for this approach.
2) Each element in the temp array contains the best maxSubArray until that index.
3) At the end we return the max of the tempArray which will contain the max subarray.
"""

class Solution:
    def maxSubArray(self, nums):
        tempArray = [0] * len(nums)
        tempArray[0] = nums[0]
        index = 1
        for number in nums[1:]:
            tempArray[index] = max(nums[index], nums[index] + tempArray[index - 1]) 
            index += 1
        return max(tempArray)
    


runThis = Solution()
final_results = runThis.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(final_results) 