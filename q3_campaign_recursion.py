# 學號: d1420592
# a = 5, b = 9, c = 2, s = 2
student_id = "d1420592"
a, b, c, s = 5, 9, 2, 2

# 1. 產生每日費用與查詢天數 n
daily_spend = [
    100 + 10 * a, 
    150 + 10 * b, 
    0, 
    200 + 10 * c, 
    50 + 10 * s
]
n = 3 + c % 3

# 2. 定義遞迴函數
def cumulative_spend(daily_spend, n):
    # 基準條件：n=0 時，累計費用為 0
    if n == 0:
        return 0
    # 遞迴步驟：前 n-1 天的累計費用 + 第 n 天的費用（索引值為 n-1）
    return cumulative_spend(daily_spend, n - 1) + daily_spend[n - 1]

# 3. 印出學號、每日費用與指定天數之累積費用
print(f"學號: {student_id}")
print(f"每日費用 (daily_spend): {daily_spend}")
print(f"指定查詢天數 n: {n}")
print(f"前 {n} 天累計費用: {cumulative_spend(daily_spend, n)} 元\n")

# 4. 依序印出前 0 至 5 天的累計費用
print("=== 每日累計費用檢驗 ===")
for i in range(6):
    total = cumulative_spend(daily_spend, i)
    print(f"前 {i} 天累計費用: {total} 元")

# 5. 驗證空資料輸入
test_empty = cumulative_spend([], 0)
print(f"\n呼叫 cumulative_spend([], 0) 結果: {test_empty}")
