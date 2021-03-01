"""

504. Base 7
The easiest way to convert a number to another base is through the division method.
The other code takes care of the sign, if any.
"""

class Solution:
    def convertToBase7(self, num: int) -> str:
        remainder = 0
        sign = ""
        if num < 0:
            num = -num
            sign = "-"
        result = ""
        while num >= 7:
            remainder = num % 7
            num = num // 7
            result += str(remainder)
        result = str(num) + result[::-1]
        return sign + result


runThis = Solution()
final_results = runThis.convertToBase7(-7)
print(final_results) 