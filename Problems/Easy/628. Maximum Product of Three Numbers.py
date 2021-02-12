"""

628. Maximum Product of Three Numbers

Since the question involves 3 numbers we need to keep a few things in mind.
1. The product of 3 largest positive numbers is a larger positive.
2. The product of 2 least negative numbers and 1 large positive number is a larger positive.

For this matter, we need to account for both the cases. 
We are ideally sorting the nums list and looking for both condition.

The computation below is to find those 3 greatest and 2 smallest numbers.

We then return the max between the two conditions.

"""
import math

class Solution:
    def maximumProduct(self, nums) -> int:
        greatest = [-math.inf] * 3
        smallest = [math.inf]* 2
        for num in nums: 
            if num >= greatest[2]:
                greatest[:-1] = greatest[1:]
                greatest[2] = num
            elif num >= greatest[1]:
                greatest[:-1] = greatest[1:]
                greatest[1] = num
            elif num >= greatest[0]:
                greatest[0] = num
                
            if num <= smallest[0]:
                smallest[1] = smallest[0]
                smallest[0] = num
            elif num <= smallest[1]:
                smallest[1] = num
        return max(greatest[0]*greatest[1]*greatest[2], smallest[0]*smallest[1]*greatest[2])



runThis = Solution()
final_results = runThis.maximumProduct([-5,3,9,9,9])
print(final_results) 