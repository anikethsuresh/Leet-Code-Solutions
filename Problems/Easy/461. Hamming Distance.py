"""

461. Hamming Distance
Simple question to find the location where the two values do not overlap. The only other matter to account for is when
the length of the two ints are not the same, which is what I'm doing in the first two lines in the while loop.
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = format(x, 'b')
        y = format(y, 'b')
        counter = 0
        indexX = len(x) - 1
        indexY = len(y) - 1
        while indexX > -1 or indexY > -1:
            valueX = int(x[indexX]) if indexX > -1 else 0
            valueY = int(y[indexY]) if indexY > -1 else 0
            if valueX != valueY:
                counter += 1
            indexX -= 1
            indexY -= 1
        return counter

runThis = Solution()
final_results = runThis.hammingDistance(1, 4)
print(final_results) 