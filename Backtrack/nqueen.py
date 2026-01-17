"""
回溯算法：n 皇后

参数：
    row: 当前需要放置皇后的行号
    n: 棋盘大小
    state: 棋盘状态，2D 列表
    res: 存储所有解的列表
    cols: 列是否被占用的标记数组
    diags1: 主对角线是否被占用的标记数组（从左上到右下）
    diags2: 次对角线是否被占用的标记数组（从左下到右上）
"""
def backtrack(
    row: int,
    n: int,
    state: list[list[str]],
    res: list[list[list[str]]],
    cols: list[bool],
    diags1: list[bool],
    diags2: list[bool],
):
    # 递归基例：所有行都已放置皇后，则找到一个完整解
    if row == n:
        # 深拷贝当前棋盘状态并加入结果集
        res.append([list(row) for row in state])
        return
    
    # 在当前行尝试在每一列放置皇后
    for col in range(n):
        # 根据行列号计算主对角线和次对角线的编号
        # 主对角线：row - col 的值相同的格子在同一条主对角线上，加 n-1 是为了避免负数
        diag1 = row - col + n - 1
        # 次对角线：row + col 的值相同的格子在同一条次对角线上
        diag2 = row + col
        
        # 剪枝：检查该位置是否合法
        # 条件：该列无皇后 且 主对角线无皇后 且 次对角线无皇后
        if not cols[col] and not diags1[diag1] and not diags2[diag2]:
            # 做选择：将皇后放置在该格子
            state[row][col] = "Q"
            # 同时标记该列和两条对角线为已占用
            cols[col] = diags1[diag1] = diags2[diag2] = True
            
            # 递归到下一行，继续放置皇后
            backtrack(row + 1, n, state, res, cols, diags1, diags2)
            
            # 撤销选择：恢复该格子的状态
            state[row][col] = "#"
            # 取消标记该列和两条对角线
            cols[col] = diags1[diag1] = diags2[diag2] = False

"""
求解 n 皇后问题

使用回溯算法找出在 n×n 棋盘上放置 n 个皇后的所有方案，
使得任意两个皇后都不在同一行、列或对角线上。

参数：
    n: 棋盘大小和皇后数量

返回：
    包含所有合法方案的列表，每个方案是一个 n×n 的棋盘状态
"""
def n_queens(n: int) -> list[list[list[str]]]:
    # 初始化 n×n 大小的棋盘，其中 'Q' 代表皇后，'#' 代表空位
    state = [["#" for _ in range(n)] for _ in range(n)]
    
    # 记录列的占用情况，索引 i 对应第 i 列
    cols = [False] * n
    
    # 记录主对角线的占用情况（从左上到右下）
    # 共有 2n-1 条主对角线，索引范围 0 到 2n-2
    diags1 = [False] * (2 * n - 1)
    
    # 记录次对角线的占用情况（从左下到右上）
    # 共有 2n-1 条次对角线，索引范围 0 到 2n-2
    diags2 = [False] * (2 * n - 1)
    
    # 存储所有找到的解
    res = []
    
    # 从第 0 行开始进行回溯求解
    backtrack(0, n, state, res, cols, diags1, diags2)

    return res

"""Driver Code"""
if __name__ == "__main__":
    n = 4
    solutions = n_queens(n)

    print(f"输入棋盘长宽为 {n}")
    print(f"共有 {len(solutions)} 种摆放方案：\n")
    for state in solutions:
        print("--------------------")
        for row in state:
            print(row)
       