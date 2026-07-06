class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod, zero_cnt = 1, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_cnt += 1
            else: 
                prod *= nums[i]

        if zero_cnt >= 2:
            return [0] * len(nums)

        output = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_cnt == 0:
                output[i] = prod // c
            elif zero_cnt == 1:
                if c == 0:
                    output[i] = prod
                else:
                    output[i] = 0




        return output
        