# solution class
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        star = 1
        counter = 0
        maxims = []
    
        for i in range(0, len(nums)):
            if nums[i] == star:
                counter += 1
            else:
                maxims.append(counter)
                counter = 0
            
        if nums[len(nums) - 1] == star:
            maxims.append(counter)
    
        return max(maxims)

# example        
solution = Solution()
result = solution.findMaxConsecutiveOnes([0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1]);
print(result)
