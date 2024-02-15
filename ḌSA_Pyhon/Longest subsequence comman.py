def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)

    # Creating a table to store the lengths of LCS
    L = [[0] * (n + 1) for i in range(m + 1)]

    # Building the L[m+1][n+1] table in bottom-up fashion
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # Following code is used to print LCS
    index = L[m][n]
    lcs_length = index

    # Create a character array to store the lcs string
    lcs = [""] * (index + 1)
    lcs[index] = ""

    # Start from the right-most-bottom-most corner and
    # one by one store characters in lcs[]
    i = m
    j = n
    while i > 0 and j > 0:

        # If current character in X[] and Y are same, then
        # current character is part of LCS
        if X[i - 1] == Y[j - 1]:
            lcs[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1

        # If not same, then find the larger of two and
        # go in the direction of larger value
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs), lcs_length

# Example usage:
X = "ABCDGH"
Y = "AEDFHR"
lcs_string, length = longest_common_subsequence(X, Y)
print("Longest Common Subsequence:", lcs_string)
print("Length of LCS:", length)
