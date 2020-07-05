# solution class
class Solution(object):
    def checkIfExist(self, arr):

        for i in range(0, len(arr)):
            
            star = arr[i] * 2
        
            for j in range(0, len(arr)):
                if j != i and star == arr[j]:
                    return True
        
        return False
        
# example
solution = Solution()
result = solution.checkIfExist([10,2,5,3])
print(result)
