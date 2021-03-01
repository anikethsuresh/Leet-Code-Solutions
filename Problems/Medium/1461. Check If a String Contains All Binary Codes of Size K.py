"""

1461. Check If a String Contains All Binary Codes of Size K

The intuitive method would be to go through all the codes of size k and convert the value to base 10 and check it, 
but the fastest and simplest method is here below.

We maintain a set.
Add all the codes of size k to this set.
If the number of elements in the set is equal to 2^k then we have all the required codes, else False, we do not have them all.
"""

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        all_codes = set()
        for i in range(len(s)-k+1):
            current_code = s[i:i+k]
            all_codes.add(current_code)
        return len(all_codes) == pow(2,k)


runThis = Solution()
final_results = runThis.hasAllCodes("00110", 2)
print(final_results) 