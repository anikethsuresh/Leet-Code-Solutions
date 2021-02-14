"""

67. Add Binary

Simple question to sum two binary strings.
I could have made it more faster and succinct, but its all good.
"""

ONE = ord("1")

class Solution:
    def addBinary(self, a, b) :
        indexA  = len(a)- 1
        indexB = len(b) - 1
        carry = 0
        result = ""
        while indexA >= 0 or indexB >= 0:
            currentBitA = a[indexA] if indexA > -1 else '0'
            currentBitB = b[indexB] if indexB > -1 else '0'
            currentBitA = 1 if ord(currentBitA) == ONE else 0
            currentBitB = 1 if ord(currentBitB) == ONE else 0
            total = currentBitA + currentBitB + carry
            if total == 0:
                result += "0"
                carry = 0
            elif total == 1:
                result += "1"
                carry = 0
            elif total == 2:
                result += "0"
                carry = 1
            elif total == 3:
                result += "1"
                carry = 1
            indexA -=1
            indexB -=1
        return result[::-1] if carry == 0 else "1" + result[::-1]
            



runThis = Solution()
final_results = runThis.addBinary("11","1")
print(final_results) 