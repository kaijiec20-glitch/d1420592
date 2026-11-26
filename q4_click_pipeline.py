# 學號: d1420592
# a = 5, b = 9, c = 2
student_id = "d1420592"
a, b, c = 5, 9, 2

# 1. 產生原始點擊資料與門檻
raw_clicks = [
    str(10 + a), 
    "0", 
    "", 
    " " + str(5 + b) + " ", 
    "   ", 
    str(15 + c), 
    str(5 + b)
]
min_clicks = 5 + b

# 2. 定義 select_clicks 函數
def select_clicks(raw_clicks, min_clicks=10):
    # 1) map() 搭配 lambda 去掉每筆文字的頭尾空白
    stripped = map(lambda s: s.strip(), raw_clicks)
    # 2) filter(None, ...) 刪掉空字串
    non_empty = filter(None, stripped)
    # 3) map(int, ...) 轉整數
    numbers = list(map(int, non_empty))
    # 4) filter() 搭配 lambda 篩選出大於或等於 min_clicks 的項目
    qualified = list(filter(lambda x: x >= min_clicks, numbers))
    
    return (numbers, qualified)

# 3. 呼叫函式並印出結果
numbers, qualified = select_clicks(raw_clicks, min_clicks=min_clicks)
qualified_count = len(qualified)
qualified_sum = sum(qualified)

print(f"學號: {student_id}")
print(f"合格門檻 (min_clicks): {min_clicks}")
print(f"清理後的整數串列 (numbers): {numbers}")
print(f"合格點擊串列 (qualified): {qualified}")
print(f"合格素材筆數: {qualified_count} 筆")
print(f"合格素材點擊合計: {qualified_sum} 次\n")

# 4. 使用 sorted 與 enumerate 印出排名
print("=== 合格素材排名 (由大到小) ===")
sorted_qualified = sorted(qualified, reverse=True)
for rank, clicks in enumerate(sorted_qualified, start=1):
    print(f"第 {rank} 名: {clicks} 次點擊")
print()

# 5. 使用門檻 100 進行測試
print("=== 門檻 100 測試 ===")
_, qualified_100 = select_clicks(raw_clicks, min_clicks=100)
print(f"合格結果: {qualified_100}")
print(f"合格筆數: {len(qualified_100)} 筆")
print(f"合計: {sum(qualified_100)} 次")
if len(qualified_100) == 0:
    print("無符合門檻的素材")
