"""

1018. Binary Prefix Divisible By 5

Initially, I though the simplest method would be to extract each binary value, convert that to base 10 and return the list of elements which are
divisible by 5. However, I found out that this is extremely poor as this would require trememdous computation for a large input.

The issue here is also to do with overflow, if we were to keep track of the running_sum as I did below (in other languages), I might
end up overflowing (In C++ ints are 32 bit, it is possible to overflow here)


Notes:
The following solution is very intersting and is from a field of cryptographs. The proof can be found though a quick google.
I've left the poor solution in comments.

1) The most important fact to notice is that when you include a number (1/0) on the left, the value in decimal increases by a factor of 2.
If the number you include is 0, we just have to multiply that number by 2 and you're done.
If the number you include is 1, we just have to multiply that number by 2 and add 1, and you're done. This is exactly what I have done.

The interesting facet is in the formula below:

(ab+c)%5 = ((a%5)*(b%5)+c%5) %5

Here, a is the current running_sum, b is 2 and c is either 0/1. The %5 is from the question, since we need to check the divisibility with 5.
This prevents us from having a "results" array as I did in the first poor solution.
"""


class Solution:
    # def prefixesDivBy5(self, A):
    #     results = []
    #     for i,value in enumerate(A):
    #         current_binary = A[:i + 1]
    #         # print(current_binary)
    #         base_10 = self.getBase10(current_binary)
    #         # print(base_10)
    #         results.append(True) if base_10 % 5 == 0 else results.append(False)
    #     return results
            
    # def getBase10(self, A):
    #     result = 0
    #     index = len(A) - 1
    #     power = 0
    #     while index != -1:
    #         result += A[index] * pow(2,power)
    #         index -= 1
    #         power += 1
    #     return result

    def prefixesDivBy5(self, A):
        results = []
        running_sum = 0
        for number in A:
            running_sum = (running_sum % 5 * 2 % 5 + number % 5) % 5
            results.append(True) if running_sum == 0 else results.append(False)

        return results



runThis = Solution()
final_results = runThis.prefixesDivBy5([0,1,1,1,1,1])
print(final_results) 