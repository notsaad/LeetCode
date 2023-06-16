class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cD = collections.defaultdict(set)
        rD = collections.defaultdict(set)
        sD = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in cD[c] or val in rD[r] or val in sD[(r//3, c//3)]:
                    return False
                cD[c].add(val)
                rD[r].add(val)
                sD[(r//3, c//3)].add(val)

        return True
