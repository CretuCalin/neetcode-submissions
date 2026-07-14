class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] 
        max_area = 0

        for i in range(len(heights)):
            # print("i=", i)
            # print(stack)
            # print(max_area)
            if not stack:
                stack.append((i, heights[i]))

            elif heights[i] >= stack[-1][1]:
                stack.append((i, heights[i]))

            else: 
                top_index  = i
                while stack and heights[i] < stack[-1][1]:
                    top_index, top_height = stack.pop()
                    area = top_height * (i - top_index)
                    max_area = max(max_area, area)

                stack.append((top_index, heights[i]))

        # print('Current stack', stack)
        while stack:
            top_index, top_height = stack.pop()
            area = top_height * (len(heights) - top_index)
            # print("area:", area)
            max_area = max(max_area, area)
        
        return max_area


# sol = Solution()
# sol.largestRectangleArea([2,1,5,6,2,3])

            