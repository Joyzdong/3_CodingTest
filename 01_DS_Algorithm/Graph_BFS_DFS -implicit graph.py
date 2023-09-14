C = {}
def comb(n, r):
    if r == 0 or r == n:
        return 1
    if r == 1 or r == n-1: # for 속도 개선1
        return n
    if r == 2 or r == n-2: # for 속도 개선2
        return int(n*(n-1)/2)
    if (n, r) not in C:
        C[(n, r)] = comb(n-1, r) + comb(n-1, r-1)
    return C[(n, r)]

r = comb(9, 8)
print(r)