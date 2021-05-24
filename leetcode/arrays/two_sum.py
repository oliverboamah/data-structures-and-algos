''''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''
# solution class
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dictionary = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dictionary and dictionary[complement] != i:
                return [i, dictionary[complement]]
            
            dictionary.update({nums[i]: i})
            
# example            
result = Solution.twoSum([2, 7, 11, 15])
print(result)
