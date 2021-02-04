"""
1576. Replace All ?'s to Avoid Consecutive Repeating Characters

Notes: 
Interestingly, you do not need more than 3 chracters to ensure that there are no repeating consecutive characters.
For this reason, I have only used a, b and c.

I loop through every character, stopping when the current character is "?".
I get the "before" and "after" characters, loop through the alphabets (a,b and c) and replace the "?",
ensuring that the added character is not the same as "before" and "after".
"""

class Solution:
    def modifyString(self, s: str) -> str:
        alphabets = "abc"
        # Strings are immutable. In order to modify them I convert it to a list and convert it back to a string at the end
        s = list(s)
        for i in range(len(s)):
            if s[i] == "?":
                # Using X as an arbitrary character which will never appear, since the input consists only of lowercase alphabets 
                before = "X" if i-1 < 0 else s[i-1]
                after = "X" if i+1 >= len(s) else s[i+1]
                replace = "X"
                for j in alphabets:
                    if j != before and j!=after:
                        # This is the candidate character to be used to replace the "?"
                        replace = j
                        break
                s[i] = replace
        # Convert the list to a string
        return "".join(s)


runThis = Solution()
final_results = runThis.modifyString("??yw?ipkj?")
print(final_results) 
# abywaipkja