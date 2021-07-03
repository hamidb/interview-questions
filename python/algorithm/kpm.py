# Knuth-Morris-Pratt algorithm for string matching.
# T: O(N+N)
# S: O(M)
def kpm(self, haystack: str, needle: str) -> int:
    # length of (proper) prefix that is also suffix.
    # T: O(M)  # average
    # T: Worst case is hard to compute.
    # S: O(M)
    def lps(needle):
        L = len(needle)
        lps = L * [0]
        i = 1
        l = 0
        while i < L:
            if needle[i] == needle[l]:
                l += 1
                lps[i] = l
                i += 1
            else:
                if l == 0:  # beginning and not matched.
                    lps[i] = 0
                    i += 1
                else:
                    l = lps[l-1]  # tricky part
        return lps

    if needle == '':
        return 0
    L1 = len(haystack)
    L2 = len(needle)
    lps = lps(needle)
    i, j = 0, 0
    while i < L1:
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j-1]  # length of (proper) prefix that is also suffix.
            else:
                i += 1  # start of the pattern
        if j == L2:
            return i-j
    return -1
