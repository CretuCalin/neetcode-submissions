class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = [0] * len(temperatures)
        stack.append([temperatures[0], 0])
        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                low_temp, low_temp_index = stack.pop()
                results[low_temp_index] = i - low_temp_index

            stack.append([temperatures[i], i])

        return results




        