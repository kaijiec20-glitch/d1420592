# 學號: d1420592
# 取最後三碼: a = 5, b = 9, c = 2
student_id = "d1420592"
a, b, c = 5, 9, 2

# 1. 定義 ad_report 函數
def ad_report(impressions, clicks, target=3.0):
    if impressions == 0:
        return (None, False)
    
    ctr = (clicks / impressions) * 100
    passed = ctr >= target
    return (ctr, passed)

# 2. 產生資料
ads = [
    ("搜尋廣告", 1000 + 100 * a, 30 + 5 * b),
    ("社群廣告", 1200 + 100 * b, 24 + 4 * c),
    ("影音廣告", 0, 0),
]
target = 2.5 + 0.1 * c

# 3. 印出學號與個人門檻
print(f"學號: {student_id}")
print(f"個人門檻 (Target): {target:.2f}%\n")

# 4. 逐筆計算並印出結果
print(f"{'廣告名稱':<8} | {'曝光次數':<8} | {'點擊次數':<8} | {'CTR':<8} | {'是否達標':<6}")
print("-" * 60)

passed_count = 0
for name, imp, clk in ads:
    ctr, passed = ad_report(imp, clk, target=target)
    
    # 格式化 CTR 顯示
    if ctr is None:
        ctr_display = "N/A"
    else:
        ctr_display = f"{ctr:.2f}%"
        
    if passed:
        passed_count += 1
        
    print(f"{name:<10} | {imp:<12} | {clk:<12} | {ctr_display:<10} | {str(passed):<6}")

print("-" * 60)
print(f"達標廣告總數: {passed_count} 筆\n")

# 5. 驗證預設門檻與零點擊
print("=== 驗證測試 ===")
test_1 = ad_report(1000, 30)
test_2 = ad_report(1000, 0)
print(f"ad_report(1000, 30) 回傳值: {test_1} (預設門檻 3.0%，CTR為 3.0%，應為 True)")
print(f"ad_report(1000, 0) 回傳值: {test_2} (CTR為 0.0%，應為 False)")
