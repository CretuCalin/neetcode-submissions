class Solution:

    def _create_freq_dict(self, nums: List[int]) -> Dict[int, int]:
        freq_dict = {}
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 0
        return freq_dict

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num2freq = self._create_freq_dict(nums)

        freq2num = []
        for num, freq in num2freq.items():
            freq2num.append([freq, num])

        freq2num.sort()

        return_list = []

        while len(return_list) < k:
            return_list.append(freq2num.pop()[1])
        return return_list


sol = Solution()
sol.topKFrequent([4,1,-1,2,-1,2,3], 2)