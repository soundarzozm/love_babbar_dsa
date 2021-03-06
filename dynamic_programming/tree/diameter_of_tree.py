def solve(root):

    #Base cases
    if root == None:
        return 0

    #Hypothesis
    left = solve(root.left, result)
    right = solve(root.right, result)

    #Induction
    i_am_not_root = 1 + max(left, right)
    i_am_root = 1 + left + right
    ans = max(i_am_root, i_am_not_root)
    result = max(ans, result)

    return i_am_not_root

if __name__ == "__main__":

    solve.result = float('-inf')

    solve(root)
    print(solve.result)
