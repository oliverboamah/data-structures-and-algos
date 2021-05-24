# solution class
class Solution:
    def duplicateZeros(self, arr) -> None:
        
        star = 0
        i = 0
        while i < len(arr):
            if arr[i] == star:
                for j in range(len(arr)-1, i, -1):
                    arr[j] = arr[j-1]
                i += 1
            i += 1
        
        return arr;
        
# example
solution = Solution()
result = solution.duplicateZeros([1,0,2,3,0,4,5,0])
print(result)
