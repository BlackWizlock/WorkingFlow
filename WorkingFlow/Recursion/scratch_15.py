def c_fun(n_fun, k_fun):
    if k_fun > n_fun:
        return 0
    if k_fun == 0:
        return 1
    return c_fun(n_fun - 1, k_fun) + c_fun(n_fun - 1, k_fun - 1)


n, k = map(int, input().split())
print(c_fun(n, k))