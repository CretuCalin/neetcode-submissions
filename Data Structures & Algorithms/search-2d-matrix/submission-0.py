class Solution:
    def searchMatrix(self, matrix, target):
        first_row = [x[0] for x in matrix]

        l = 0 
        r = len(first_row) - 1
        
        while l <= r:
            # print(l, r)

            middle = int((l+r) / 2)

            if target > first_row[middle]:
                l =  middle + 1

            elif target < first_row[middle]:
                r =  middle - 1
            if first_row[middle] == target:
                return True

        if matrix[r][0] < target:
            search_row = matrix[r]
        else:
            search_row = matrix[l]

        # print(search_row)
        l = 0
        r = len(search_row) - 1
        while l <= r:
            middle = int((l+r) / 2)

            if target > search_row[middle]:
                l =  middle + 1

            elif target < search_row[middle]:
                r =  middle - 1
            if search_row[middle] == target:
                return True

        return False

# sol = Solution()
# # print(sol.searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10))
# print(sol.searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 40))
            