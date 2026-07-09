class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = []
        for i in range(len(temperatures)):
            res = 0
            j = i + 1

            while j < len(temperatures):
                if temperatures[j] > temperatures[i]:
                    res = j - i
                    break
                j += 1
            results.append(res)

        return results


        