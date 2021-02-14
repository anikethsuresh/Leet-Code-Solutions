"""

26. Remove Duplicates from Sorted Array

Easy question here. 

All you need to do is check that the next number is the same as the current number,
if it is then we pop that number, if not then we iterate through the list
"""

class Solution:
    def removeDuplicates(self, nums):
        current = 0
        while current < len(nums) - 1:
            next_val = current + 1
            while nums[current] == nums[next_val]:
                nums.pop(next_val)
                if next_val >= len(nums): break
            current += 1
        return len(nums)

runThis = Solution()
final_results = runThis.removeDuplicates([1,1])
print(final_results) 
        