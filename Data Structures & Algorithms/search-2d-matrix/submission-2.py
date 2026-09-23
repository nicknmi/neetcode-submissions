class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        lowerRow = 0
        midRow = len(matrix) // 2
        upperRow = len(matrix) - 1

        n = len(matrix[0]) - 1

        while lowerRow <= midRow:
            # if within range, we've found the correct row
            if target >= matrix[midRow][0] and target <= matrix[midRow][n]:
                break
            
            if target > matrix[midRow][0]:
                lowerRow = midRow + 1
            else:
                upperRow = midRow - 1

            midRow = (upperRow + lowerRow) // 2


        lowerCol = 0
        upperCol = n
        midCol = (upperCol + lowerCol) // 2
        
        while lowerCol <= midCol:
            if matrix[midRow][midCol] == target:
                return True

            if target > matrix[midRow][midCol]:
                lowerCol = midCol + 1
            else:
                upperCol = midCol - 1

            midCol = (upperCol + lowerCol) // 2

        
        return False
