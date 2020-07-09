# solution class
class Solution(object):
    def replaceElements(self, arr):
        
        for i in range(0, len(arr)):
            sub_list = arr[i+1: len(arr)]
            
            if len(sub_list) > 0:
                maximum = max(sub_list)
                arr[i] = maximum
        
        arr[len(arr) -1]  = -1
        
        return arr
        
# example        
solution = Solution()
result = solution.replaceElements([17,18,5,4,6,1])
print(result)
