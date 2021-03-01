"""

1051. Height Checker

Once the list is sorted, go through the elements and check the positions where the students are out of position.
The number of students out of position are the ones who need to be moved.
"""

class Solution:
    def heightChecker(self, heights):
        original_heights = heights.copy()
        heights.sort()
        counter = 0
        for i in range(len(heights)):
            if heights[i] != original_heights[i]:
                counter += 1
        return counter


runThis = Solution()
final_results = runThis.heightChecker([1,1,4,2,1,3])
print(final_results) 