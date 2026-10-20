class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])
        top, bottom = 0, rows-1
        while top<=bottom:
            current_row = (top+bottom)//2
            if matrix[current_row][-1] < target:
                top = current_row + 1
            elif matrix[current_row][0] > target:
                bottom = current_row-1
            else:
                break
        if not top<=bottom:
            return False
        current_row = (top+bottom)//2
        l, r = 0, cols-1

        while l<=r:
            mid = (l + r)//2
            if matrix[current_row][mid] < target:
                l = mid + 1
            elif matrix[current_row][mid] > target:
                r = mid - 1
            else:
                return True
        return False

