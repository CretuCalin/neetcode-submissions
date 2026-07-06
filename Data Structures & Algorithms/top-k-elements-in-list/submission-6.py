import heapq
class Solution:

    def _create_freq_dict(self, nums: List[int]) -> Dict[int, int]:
        freq_dict = {}
        for num in nums:
            freq_dict[num] = 1 + freq_dict.get(num, 0)
        return freq_dict

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num2freq = self._create_freq_dict(nums)


        heap = []
        for num in num2freq.keys():
            heapq.heappush(heap, (num2freq[num], num))
            if len(heap) > k:
                heapq.heappop(heap)


        return_list = []

        while len(return_list) < k:
            return_list.append(heap.pop()[1])
        return return_list