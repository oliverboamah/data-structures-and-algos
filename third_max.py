'''
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''

# solution class 
class Solution(object):
    def thirdMax(self, nums):
        
        # corny case
        if len(nums) < 3:
            return max(nums)
            
        max_numbers = []
        
        for x in range(3):
            
            if len(nums) <= 0:
                break
            else:
                max_number = nums[0]
                for i in range(len(nums)):
                    if max_number < nums[i]:
                        max_number = nums[i]
                
                max_numbers.append(max_number)
        
                # delete first maximum number from list
                nums = self.deleteValue(nums, max_number)
          
        return max(max_numbers) if len(max_numbers) < 3 else min(max_numbers)

    def deleteValue(self, nums, value):
        new_nums =  []
        for i in range(len(nums)):
            if value != nums[i]:
                new_nums.append(nums[i])
        
        return new_nums

# example
result = Solution().thirdMax([2, 2, 3, 1])
print(result)
