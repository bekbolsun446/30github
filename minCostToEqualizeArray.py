def minCostToEqualizeArray(nums, cost1, cost2):
    ma, mi = max(nums), min(nums)
    n = len(nums)
    mod = 10 ** 9 + 7
    total = ma * n - sum(nums)

    if cost1 * 2 <= cost2 or n <= 2:
        return total * cost1 % mod

    op1 = max(0, (ma - mi) * 2 - total)
    op2 = total - op1
    res = (op1 + op2 % 2) * cost1 + op2 // 2 * cost2

    total += op1 // (n - 2) * n
    op1 %= n - 2
    op2 = total - op1
    res = min(res, (op1 + op2 % 2) * cost1 + op2 // 2 * cost2)

    for i in range(2):
        total += n
        res = min(res, total % 2 * cost1 + total // 2 * cost2)

    return res % mod
