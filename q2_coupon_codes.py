# 1. 設定學號末三碼為 tail
tail = "592"

# 2. 定義 collect_codes 函數
def collect_codes(raw_codes, saved=None):
    # 若未傳入 saved，則建立一個新的空串列，避免可變預設值問題
    if saved is None:
        result = []
    else:
        # 複製 saved，確保不修改原始的傳入串列
        result = list(saved)
    
    # 使用 set 來快速檢查是否已存在，以保持 O(1) ~ O(n) 的查詢效率
    seen = set(result)
    
    for raw_code in raw_codes:
        # 去掉頭尾空白並轉為大寫
        cleaned = raw_code.strip().upper()
        # 略過空字串
        if cleaned == "":
            continue
        # 若未重複，則加入
        if cleaned not in seen:
            result.append(cleaned)
            seen.add(cleaned)
            
    return result

# 3. 建立測試資料
saved = ["BASE"]
raw_a = [
    " welcome" + tail + " ", 
    "vip" + tail, 
    "",
    "WELCOME" + tail, 
    "   "
]
raw_b = [
    " new" + tail + " ", 
    " welcome" + tail + " "
]

# 4. 呼叫並執行活動 A 與活動 B
activity_a = collect_codes(raw_a, saved=saved)
activity_b = collect_codes(raw_b)

# 5. 印出所有結果以供檢驗
print(f"學號: d1420592")
print(f"活動 A 結果 (帶有 saved): {activity_a}")
print(f"活動 B 結果 (預設 saved=None): {activity_b}")
print(f"原始 saved 是否被修改 (應為 ['BASE']): {saved}")
print(f"原始 raw_a 是否被修改: {raw_a}")

# 6. 驗證空資料輸入
test_empty = collect_codes([])
print(f"呼叫 collect_codes([]) 結果: {test_empty}")
