def sum_numbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa

a = sum_numbers(5)
print(a)