# flat array

class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False

        ROWS = len(matrix)
        COLS = len(matrix[0])

        l = 0 
        r = ROWS * COLS - 1
        
        while l <= r:
            print("l:",l,"r:", r)

            middle = (l+r) // 2
            row = middle // COLS
            col = middle % COLS 

            middle_elem = matrix[row][col]


            if target > middle_elem:
                l =  middle + 1
            elif target < middle_elem:
                r =  middle - 1
            if middle_elem == target:
                return True

        return False
            