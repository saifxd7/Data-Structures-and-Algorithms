# -------------------------------------Combination Sum------------------------------------
def combinationSum(candidates, target):

    # input
    # unique integer candidates  = [2, 3, 6, 7]
    # target = 7

    # output
    # list of all unique combinations
    # [[2,2,3], [7]]

    result = []

    def dfs(i, curr, total):
        if total == target:
            result.append(curr[:])
            return

        if total > target or i >= len(candidates):
            return

        curr.append(candidates[i])
        dfs(i, curr, total + candidates[i])
        curr.pop()
        dfs(i+1, curr, total)

    dfs(0, [], 0)
    return result
