# solution class
class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
       
        for i in range(0, len(nums2)):
            nums1[m+i] = nums2[i]
          
        nums1.sort()
        
        return nums1
        

# example        
solution = Solution()
result = solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
print(result)
