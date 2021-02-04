"""
401. Binary Watch

Notes: 
We loop through every single minute of the day (12 * 60 = 720 iterations),
Convert the hour and minute to binary and sum them.
If the sum == num (input to readBinaryWatch), then it is a candidate.
We append the candidate to a list after formatting the time with leading 0's for the minutes.
"""

class Solution:
    def readBinaryWatch(self, num: int):
        results = []
        for hours in range(0,12):
            for minutes in range(0,60):
                if bin(hours).count('1') + bin(minutes).count('1') == num:
                    results.append("{}:{:02d}".format(hours, minutes))
        
        return results


runThis = Solution()
final_results = runThis.readBinaryWatch(1)
print(final_results) 
# ['0:01', '0:02', '0:04', '0:08', '0:16', '0:32', '1:00', '2:00', '4:00', '8:00']