def sum_N_numbers(n):
    if n <= 1:
        return n
    else:
        return n + sum_N_numbers(n - 1)


print(sum_N_numbers(5))
