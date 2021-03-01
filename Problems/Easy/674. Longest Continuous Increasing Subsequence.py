"""

674. Longest Continuous Increasing Subsequence

Just keep track of the longest increasing subsequence. Else, reset the counter to one


"""

class Solution:
    def findLengthOfLCIS(self, nums):
        result = 0
        count = 1 if len(nums) > 0 else 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                result = max(result, count)
                count = 1
        return max(result, count)

runThis = Solution()
final_results = runThis.findLengthOfLCIS([1,3,5,7])
print(final_results) 