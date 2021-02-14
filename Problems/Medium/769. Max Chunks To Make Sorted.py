"""

769. Max Chunks To Make Sorted

Quite an interesting solution here.
The main point to recognize is that the numbers are a permutation from 0..n-1.
Keeping this in mind, at any point, we can have a chunk if the max of all the numbers we've
seen till date is equal to the index at that point. Notice how it would be a little different if 
the numbers were a permutation from 1..n or something else.

By keeping a track of this count, we can find all the chunks when we fulfil the criteria
mentioned above 

"""


class Solution:
    def maxChunksToSorted(self, arr) -> int:
        currentMax = -1
        chunks = 0
        for index, number in enumerate(arr):
            if number > currentMax:
                currentMax = number
            if currentMax == index:
                chunks += 1
        return chunks   

runThis = Solution()
final_results = runThis.maxChunksToSorted([1,0,2,3,4])
print(final_results) 