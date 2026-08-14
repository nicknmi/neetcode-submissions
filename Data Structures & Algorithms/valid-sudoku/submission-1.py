class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenCol = defaultdict(set)
        seenRow = defaultdict(set)
        seenSqr = defaultdict(set)

        for i in range(9):
            for j in range(9):

                node = board[i][j]

                if node == ".":
                    continue

                if (node in seenCol[i] or node in seenRow[j] or node in seenSqr[(i//3, j//3)]):
                    return False

                # assign the num to the col/row/sqr 
                seenCol[i].add(node)
                seenRow[j].add(node)
                seenSqr[(i//3, j//3)].add(node)

                
        return True

