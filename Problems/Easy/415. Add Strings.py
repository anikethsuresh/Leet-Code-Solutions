"""
415. Add Strings

Notes: 
Since I could not directly convert the strings to integers, I converted the character to its Unicode Equivalence, subtracted '0' in Unicode,
and this brought me to the number itself as an integer

I set two pointers at the end of each number, set the carry value to 0 and the overall result to an empty string.
I step through the two strings in reverse until we exhaust both strings.

Finally, if there is a "1" in the carry, I append that to the result (now reversed for the proper result) or return the result as is (if the carry is 0)
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ptr_num1 = len(num1) - 1
        ptr_num2 = len(num2) - 1
        carry = 0
        result = ""
        while ptr_num1 >= 0 or ptr_num2 >=0:
            val_ptr1 = ord(num1[ptr_num1]) - ord('0') if ptr_num1 >= 0 else 0
            val_ptr2 = ord(num2[ptr_num2]) - ord('0') if ptr_num2 >= 0 else 0
            addition_result = val_ptr1 + val_ptr2 + carry
            if addition_result > 9:
                carry = 1
                result += str(addition_result%10)
            else:
                carry = 0
                result += str(addition_result)
            ptr_num1 -= 1
            ptr_num2 -= 1
        return result[::-1] if carry == 0 else "1" + result[::-1]


runThis = Solution()
final_results = runThis.addStrings("408","5")
print(final_results) 