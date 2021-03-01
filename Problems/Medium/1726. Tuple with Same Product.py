"""

1726. Tuple with Same Product

Note:
itertools.product worked great for two for loops

There are two interesting cases to think about here.
The only way 4 numbers together can create the same product is in this manner.
In the sorted list of 4 numbers, a,b,c,d:
a*d == b*c.

Therefore, we first sort the list.
Then take 4 numbers in order until the end and check this condition.
Then we need to do this from the outermost numbers to the center.
For example, if the numbers are a,b,c,d,e,f.
We need to check, our condition for a*b == e*f and then b*c == d*e

This is a method I was taught in India (calculating the HCF anf LCM), and definitely helped here.
"""

class Solution:
    def tupleSameProduct(self, nums):
        if len(nums)< 4: return 0
        nums.sort()
        repetitions = []
        counter = 0
        # Left to right
        for i in range(len(nums)-4+1):
            ll,ml,mr,rr = nums[i],nums[i+1],nums[i+2],nums[i+3]
            str_version = str(ll) + str(ml) + str(ml) + str(rr)
            if ll*rr ==ml*mr and str_version not in repetitions:
                repetitions.append(str_version)
                counter += 1
        # Out to in
        ll,ml,mr,rr = 0,1,2,3 # Needs to be distinct, does not matter
        left = 0
        right = len(nums)-1
        while True:
            ll,ml,mr,rr = nums[left],nums[left+1],nums[right-1],nums[right]
            str_version = str(ll) + str(ml) + str(ml) + str(rr)
            if len(set([ll,ml,mr,rr])) != 4:
                break
            else:
                if ll*rr ==ml*mr and str_version not in repetitions:
                    counter += 1
            left += 1
            right -= 1
        return counter*8


runThis = Solution()
final_results = runThis.tupleSameProduct([1,2,4,5,10])
print(final_results) 