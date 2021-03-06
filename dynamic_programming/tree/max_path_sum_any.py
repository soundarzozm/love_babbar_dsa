import sys

def solve(root):

    #Base cases
    if root == None:
        return 0

    #Hypothesis
    left = solve(root.left, result)
    right = solve(root.right, result)

    #Induction
    i_am_not_root = max(root.data + max(left, right), root.data)
    i_am_root = root.data + left + right
    ans = max(i_am_root, i_am_not_root)
    result = max(ans, result)

    return i_am_not_root

if __name__ == "__main__":

    solve.result = -sys.maxsize

    solve(root)
    print(solve.result)
