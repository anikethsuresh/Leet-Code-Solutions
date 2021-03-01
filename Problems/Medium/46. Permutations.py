"""

46. Permutations

Absolutely mind blowing solution I had to research to figure out.
I would suggest going through the solutions in the discussion, if you don't figure it out reach out to me!

"""

class Solution:
    def permute(self, nums):
        result = []
        path = []
        def permutation(nums, path, result):
            if len(nums) == 0:
                result.append(path)
            for index, value in enumerate(nums):
                permutation(nums[:index] + nums[index+1:], path + [value], result)
        
        permutation(nums, path, result)
        return result


runThis = Solution()
final_results = runThis.permute([1,2,3])
print(final_results) 