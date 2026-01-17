def knapsack_dp_comp(wgt: list[int], val: list[int], cap: int) -> int:
    """0-1 背包：空间优化后的动态规划"""
    n = len(wgt)
    # 初始化 dp 表
    dp = [0] * (cap + 1)
    # 状态转移
    for i in range(1, n + 1):
        # 倒序遍历
        for c in range(cap, 0, -1):
            if wgt[i - 1] > c:
                # 若超过背包容量，则不选物品 i
                dp[c] = dp[c]
            else:
                # 不选和选物品 i 这两种方案的较大值
                dp[c] = max(dp[c], dp[c - wgt[i - 1]] + val[i - 1])
    return dp[cap]

'''Driver Code'''
if __name__ == "__main__":
    wgt = [10, 20, 30, 40, 50]
    val = [50, 120, 150, 210, 240]
    cap = 50
    n = len(wgt)

    # 空间优化后的动态规划
    res = knapsack_dp_comp(wgt, val, cap)
    print(f"不超过背包容量的最大物品价值为 {res}")