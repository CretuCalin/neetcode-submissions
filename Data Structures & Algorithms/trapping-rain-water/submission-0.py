class Solution:
    def trap(self, height: List[int]) -> int:
        # print("ASDASDA" + str(len(height)))
        maxl = [0] * len(height)
        maxr = [0] * len(height)

        curr_max = 0
        for i in range(1, len(height)):
            curr_max = max(curr_max, height[i-1])
            maxl[i] = curr_max

        curr_max = 0
        for i in range(len(height)-2, 0, -1):
            # print(i)
            curr_max = max(curr_max, height[i + 1])
            maxr[i] = curr_max

        # print(maxl)
        # print(maxr)
    
        water_sum = 0
        for i in range(1, len(height)-1):
            curr_water = min(maxl[i], maxr[i]) - height[i]
            if curr_water >= 0:
                water_sum += curr_water

            # print("i:{}, curr_water:{}, water_sum:{}".format(i, curr_water, water_sum))
        
        return water_sum


# sol = Solution()
# sol.trap([0,2,0,3,1,0,1,3,2,1])
