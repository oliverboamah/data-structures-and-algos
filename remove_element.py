# solution class
class Solution(object):
    def removeElement(self, nums, val):
        
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
                i -= 1
            i += 1
        
        return nums
        
# example
solution = Solution()
result = solution.removeElement([3,2,2,3], 3)
print(result)
