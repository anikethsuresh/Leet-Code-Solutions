"""

8. String to Integer (atoi)

This problem was all about handing every possible case. As you can see in the code below, I ended up with a lot of if/else conditions.

The algorithm itself is straightforward, there are however a lot of subtleties to its implementation in Python

1. We remove all leading whitespace characters. If the length of the remaining string is 0 we return 0 (weird case)
2. We take the next character. If it is "+" or "-" we need to accound the sign in the final answer.
3. For each character we come across, we first check that the character is a number (converting it to its ascii representation),
    If we encounter a non-numeric character we return the result (this would hold the current numbers at the time or 0 if the first letter
    is not numeric).
4. I now check for overflow. In the case for Python, its integers are unbounded, so we technically do not need to account for that.
however for the sake of this question I have accounted for it.
Since, 2147483647 is pow(2,31), if at any point, we come across a number which is 214748364 (no last digit) and the next digit is greater than 7 or
the number itself is greater, we need to return 2147483647. 
We need to do the same for the negative minimum int value.
5. Apart from this, we are building the integer up on line 52 (quite simple)
"""

CHAR_0 = ord("0")
TWO_POWER_32 = 2147483647

class Solution:
    def myAtoi(self, s: str) -> int:
        # Strip leading whitespace characters
        s = s.lstrip()
        # Check whether the next character is a + or - sign
        if len(s) == 0: return 0
        sign = s[0]
        result = 0
        if sign == "-" or sign == "+":
            if sign == "-":
                sign = -1
            elif sign == "+":
                sign = 1
            s = s[1:]
        else:
            sign = 1
        for index, char in enumerate(s):
            char_current = ord(char)
            if char_current - CHAR_0 > 9 or char_current - CHAR_0 < 0:
                return result * sign
            else:
                if sign == 1 and result >= TWO_POWER_32//10:
                    if char_current - CHAR_0 > 7 or result > TWO_POWER_32//10:
                        return TWO_POWER_32
                elif sign == -1 and result >= TWO_POWER_32//10:
                    if char_current - CHAR_0 > 8 or result > TWO_POWER_32//10:
                        return -(TWO_POWER_32 + 1)
                result = result * 10 + (char_current - CHAR_0)
        return result * sign


runThis = Solution()
final_results = runThis.myAtoi("-987654321werty34567")
print(final_results) 