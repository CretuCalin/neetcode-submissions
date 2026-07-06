class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_dict = {}
        for x in nums:
            if x not in count_dict:
                count_dict[x] = 'a'
            else:
                return True
        return False
        