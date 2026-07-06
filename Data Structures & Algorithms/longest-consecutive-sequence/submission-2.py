class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
    
        nums_set = set(nums)

        seq_len = 0
        max_seq_len = 0

        for num in nums_set:
            seq_len = 1
            # start of sequence
            if num-1 not in nums_set:
                value = num
                while value+1 in nums_set:
                    value += 1
                    seq_len += 1
                if seq_len > max_seq_len:
                    max_seq_len = seq_len
            else:
                continue

        return max_seq_len
