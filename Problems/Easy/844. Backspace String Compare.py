"""

844. Backspace String Compare

The main data structure used here could be a stack. Python's list could function in a similar manner.

1. Whenever we see a backspace ("#") character, we perform a pop
2. Whenever we see a regular lowercase character, we push it in to the stack.
3. We perform this operation for both strings and check that they are both the same. If they are, we return True, else False.
"""

class Solution:
    def backspaceCompare(self, S, T) -> bool:
        finalS, finalT = self.getFinalText(S), self.getFinalText(T)
        return finalS == finalT

    def getFinalText(self, text):
        result = []
        for character in text:
            if character == "#":
                if len(result) != 0:
                    result.pop()
            else:
                result.append(character)
        return "".join(result)

runThis = Solution()
final_results = runThis.backspaceCompare("a##c","#a#c")
print(final_results) 