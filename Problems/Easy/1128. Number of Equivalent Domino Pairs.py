"""

1128. Number of Equivalent Domino Pairs

The fastest way to solve this question would be to add them all to a hash set and 
then sum the count for each pair using gauss's method (or something, basically the sum of numbers from 1 to n-1).

The problem with this approach is that a list is not hashable. Due to this problem, we need to
figure out a representation for the numbers in the list where [1,2] == [2,1]. 
My solution takes the larger of the two numbers x 10 + min of the two numbers. The two numbers
would be 21 and 21, which is hashable.



"""

class Solution:
    def numEquivDominoPairs(self, dominoes) -> int:
        domino_dict = {}
        for domino in dominoes:
            domino = self.convertDomino(domino)
            if domino in domino_dict:
                domino_dict[domino] += 1
            else:
                domino_dict[domino] = 1
        total = 0
        for value in domino_dict.values():
            total += int((value * (value-1))/2)
        return total

    def convertDomino(self, domino):
        return max(domino)* 10 + min(domino)

runThis = Solution()
final_results = runThis.numEquivDominoPairs([[1,1],[2,2],[1,1],[1,2],[1,2],[1,1]])
print(final_results) 