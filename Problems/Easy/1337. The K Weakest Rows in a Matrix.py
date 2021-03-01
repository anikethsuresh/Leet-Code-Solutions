"""

1337. The K Weakest Rows in a Matrix

Brilliant question.
Rather than going through all the elements of this matrix, the quickest way to get a solution would be to traverse
the columns rather than the rows. In this manner we can know when the soldiers are done and when the civilians have begun.

If we reach the end of the matrix and still have not recieved k indices, we loop through the last column and add the indices
till we have k rows' indices.

"""
from itertools import product

class Solution:
    def kWeakestRows(self, mat, k):
        result = []
        for i, j in product(list(range(len(mat[0]))), list(range(len(mat)))):
            if i == 0:
                if mat[j][i] == 0:
                    result.append(j)
            else:
                if mat[j][i] == 0 and mat[j][i-1] == 1:
                    result.append(j)
            if len(result) == k :
                break
        if len(result) != k:
            last = len(mat[0])-1
            for i in range(len(mat)):
                if i not in result: result.append(i)
                if len(result) == k:
                    break
        return result


runThis = Solution()
final_results = runThis.kWeakestRows(
[[1,1,1,1,0,0],[1,0,0,0,0,0],[1,1,1,1,1,1]],1)
print(final_results) 