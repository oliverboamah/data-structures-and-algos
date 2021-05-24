# solution class
class Solution(object):
    def moveZeroes(self, nums):
        
        pos = 0
        
        for i in range(len(nums)):
            el = nums[i]
            if el != 0:
            
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
        
        return nums
                
# example
solution = Solution()
result = solution.moveZeroes([0,1,0,3,12])
print(result)
