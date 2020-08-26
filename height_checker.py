# question
'''
Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students that must move in order for all students to be standing in non-decreasing order of height.

Notice that when a group of students is selected they can reorder in any possible way between themselves and the non selected students remain on their seats.
'''

# solution class
class Solution(object):
    def heightChecker(self, heights):
        
        
        # corner cases
        if len(heights) == 0 or len(heights) == 1 or (len(heights) == 2 and heights[0] <= heights[1]):
            return 0
        elif len(heights) == 2 and heights[0] > heights[1]:
            return 1
        
        num_changes = 0
        
        sorted_heights = heights[:]
        sorted_heights.sort()
        
        print(heights)
        print(sorted_heights)
        
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                num_changes += 1
        
        return num_changes
        
# example
result = Solution().heightChecker([1,1,4,2,1,3])
print(result)
