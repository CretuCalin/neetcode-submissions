class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0 

        for i in range(len(heights)):
            l = r = i
            while l > 0:
                if heights[l-1] >= heights[i]:
                    l -= 1
                else:
                    break

            while r < len(heights) - 1:
                if heights[r + 1] >= heights[i]:
                    r += 1
                else:
                    break
            
            curr_h = heights[i]
            curr_w = r - l + 1
            print(r,l, heights[i])
            maxArea = max(maxArea, curr_h * curr_w)

        return maxArea