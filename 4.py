def count_ways(n, memo):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if n in memo:
        return memo[n]
    memo[n] = count_ways(n-1, memo) + count_ways(n-2, memo) + count_ways(n-3, memo)
    return memo[n]

n = 8
memo = {}
ways = count_ways(n, memo)
print('Количество вариантов:', ways)


