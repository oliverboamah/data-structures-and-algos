# solution class
class Solution(object):
    def removeDuplicates(self, nums):
        nums.sort()
        
        i = 0
        
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                del nums[i]
                i -= 1
            i += 1
                
        return nums
        
# example
solution = Solution()
result = solution.removeDuplicates([1,1,2])
print(result)
