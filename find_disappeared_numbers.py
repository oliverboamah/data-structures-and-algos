'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
'''

# solution
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        disappeared_nums = []
        for i in range(1, len(nums) + 1):
            disappeared_nums.append(i)
        
        for i in range(len(nums)):
            if nums[i] == disappeared_nums[nums[i] - 1]:
                disappeared_nums[nums[i] - 1] = 0
                
        nums = []
                
        for i in range(len(disappeared_nums)):
            if disappeared_nums[i] != 0:
                nums.append(disappeared_nums[i])
        
        return nums

# example
result = Solution().findDisappearedNumbers[4,3,2,7,8,2,3,1]
