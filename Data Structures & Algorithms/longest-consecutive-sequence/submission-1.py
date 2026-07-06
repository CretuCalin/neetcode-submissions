class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()

        max_sequence = 1
        current_seqence = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] == nums[i - 1] + 1:
                current_seqence += 1
                if max_sequence < current_seqence:
                    max_sequence = current_seqence
            else:
                current_seqence = 1

        return max_sequence
