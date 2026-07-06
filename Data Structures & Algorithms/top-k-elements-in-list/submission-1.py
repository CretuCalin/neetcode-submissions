class Solution:

    def _create_freq_dict(self, nums: List[int]) -> Dict[int, int]:
        freq_dict = {}
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 0
        return freq_dict

    def computeLeastFreq(self, my_list: List[int], num2freq: Dict[int, int]) -> (int, int, int):
        # returns min_freq, number_at_min_freq, min_freq_index
        print("Start computeLeastFreq")
        min_freq = 10^4 + 1
        number_at_min_freq = 1001
        min_freq_index = float('-inf')
        for index, number in enumerate(my_list):
            freq = num2freq[number]
            if min_freq >= freq:
                min_freq = freq
                number_at_min_freq = number
                min_freq_index = index
            print("min_freq: {}, number_at_min_freq: {}, min_freq_index:{}".format(min_freq, number_at_min_freq, min_freq_index))
    
        print("End computeLeastFreq")
        
        return min_freq, number_at_min_freq, min_freq_index

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num2freq = self._create_freq_dict(nums)
        print("Start")
        print(num2freq)
        # freq2num = {}
        # for key in num2freq:
        #     freq2num[num2freq[key]] = key

        return_list = []
        min_freq = 10^4 + 1
        number_at_min_freq = 1001
        min_freq_index = float('-inf')
        for index, (number, freq) in enumerate(num2freq.items()):
            if len(return_list) < k:
                return_list.append(number)
                if min_freq >= freq:
                    min_freq = freq
                    number_at_min_freq = number
                    min_freq_index = len(return_list) - 1
                print("index: {}, number: {}, freq: {}, return_list: {}, min_freq: {}, number_at_min_freq: {}, min_freq_index: {} ".format(index, number, freq, return_list, min_freq, number_at_min_freq, min_freq_index))
                # print(number, freq, return_list, min_freq, number_at_min_freq, min_freq_index)
            else:
                
                if freq <= min_freq:
                    print("if index: {}, number: {}, freq: {}, min_freq: {}".format(index, number, freq, min_freq))
                    continue
                else:
                    print("else index: {}, number: {}, freq: {}, min_freq: {}".format(index, number, freq, min_freq))
                    # delete least frequest
                    del return_list[min_freq_index]
                    print("after delete -> return_list: {}, min_freq_index: {}".format(return_list, min_freq_index))
                    # append to list
                    return_list.append(number)
                    print("after append -> return_list: {}, min_freq_index: {}".format(return_list, min_freq_index))

                    # recompute least frequent
                    print("before recompute -> return_list: {}, num2freq: {}".format(return_list, num2freq))
                    min_freq, number_at_min_freq, min_freq_index = self.computeLeastFreq(return_list, num2freq)
                    print("after recompute -> min_freq: {}, number_at_min_freq: {}, min_freq_index: {}".format(min_freq, number_at_min_freq, min_freq_index))


        return return_list


sol = Solution()
# sol.topKFrequent([4,1,-1,2,-1,2,3], 2)

print(sol.computeLeastFreq([4, -1], {4: 0, 1: 0, -1: 1, 2: 1, 3: 0}))
# print(sol._create_freq_dict([]))
# print(sol._create_freq_dict([1, 2, 3, 4]))
# print(sol._create_freq_dict([-2, 5, 7]))
# print(sol._create_freq_dict([1, 2, 2, 4, 4, 6]))