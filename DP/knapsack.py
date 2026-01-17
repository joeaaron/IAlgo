"""
0-1 背包：空间优化后的动态规划

使用一维 DP 数组解决 0-1 背包问题，相比二维数组大幅节省空间。
关键优化：倒序遍历容量，避免同一件物品被重复选择。

参数：
    wgt: 各物品的重量数组
    val: 各物品的价值数组
    cap: 背包的最大容量

返回：
    背包能装下的最大物品价值
"""
def knapsack_dp_comp(wgt: list[int], val: list[int], cap: int) -> int:
    n = len(wgt)
    
    # 初始化 DP 表
    # dp[c] 表示容量为 c 时的最大价值
    # 初始值全为 0（空背包的价值为 0）
    dp = [0] * (cap + 1)
    
    # 状态转移：遍历每一件物品
    for i in range(1, n + 1):
        # 倒序遍历背包容量
        # 倒序的目的：保证每件物品只被考虑一次
        # 如果顺序遍历，会在同一轮循环中重复使用同一件物品
        for c in range(cap, 0, -1):
            # 检查当前物品是否超过背包容量
            if wgt[i - 1] > c:
                # 超过容量，无法选择该物品，保持原值
                dp[c] = dp[c]
            else:
                # 容量充足，比较两种方案的价值：
                # 1. 不选物品 i：dp[c]（原价值）
                # 2. 选物品 i：dp[c - wgt[i - 1]] + val[i - 1]（剩余容量的最优价值 + 该物品价值）
                # 选择价值更高的方案
                dp[c] = max(dp[c], dp[c - wgt[i - 1]] + val[i - 1])
    
    # 返回容量为 cap 时的最大价值
    return dp[cap]

'''Driver Code'''
if __name__ == "__main__":
    # 测试数据
    wgt = [10, 20, 30, 40, 50]  # 各物品的重量
    val = [50, 120, 150, 210, 240]  # 各物品的价值
    cap = 50  # 背包容量
    n = len(wgt)

    # 求解 0-1 背包问题（空间优化版本）
    res = knapsack_dp_comp(wgt, val, cap)
    print(f"不超过背包容量的最大物品价值为 {res}")