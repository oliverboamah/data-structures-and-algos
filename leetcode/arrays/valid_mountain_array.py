# solution class
class Solution(object):
    def validMountainArray(self, A):
   
        if len(A) < 3:
            return False
        
        maximum = max(A)
        max_index = A.index(maximum)
        
        if max_index == 0 or max_index == len(A) - 1:
            return False
        
        for i in range(0, max_index):
            
            if A[i] >= A[i+1]:
                return False
        
        for i in range(len(A)-1, max_index, -1):
            
            if A[i] >= A[i-1]:
                return False
        
        return True

# example
solution = Solution()
result = solution.validMountainArray([0,3,2,1])
print(result)
