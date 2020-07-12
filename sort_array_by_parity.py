# solution class
class Solution(object):
    def sortArrayByParity(self, A):
       
        pos = 0
    
        for i in range(len(A)):
        
            if A[i] % 2 == 0:
                A[pos], A[i] = A[i], A[pos]
                pos += 1
        
        return A
                
# example
solution = Solution()
result = solution.sortArrayByParity([3,1,2,4])
print(result)
