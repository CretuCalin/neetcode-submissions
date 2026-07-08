class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sols = set()


        for i in range(0, len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] == 0:
                    solution = [nums[i], nums[j], nums[k]]
                    solution.sort()
                    solution = tuple(solution)
                    if solution not in sols:
                        sols.add(solution)
                    j += 1
        return [list(sol) for sol in sols]