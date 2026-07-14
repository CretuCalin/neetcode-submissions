class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        l = 0
        r = len(nums) - 1

        while l <= r:

            middle = int((l + r) / 2)
            if nums[middle] == target:
                return middle
            
            if target < nums[middle]:
                r = middle - 1
            else: 
                l = middle + 1

        return -1