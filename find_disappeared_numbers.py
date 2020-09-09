'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
'''

# solution
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        result = []
        for i in range(len(nums)):
            j = abs(nums[i]) - 1
            nums[j] = abs(nums[j]) * -1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        
        return result

# example
result = Solution().findDisappearedNumbers[4,3,2,7,8,2,3,1]
