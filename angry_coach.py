point = int(input("得点: "))
turnover = int(input("ターンオーバー数: "))

print("===== 試合後 =====")

if point >= 20 and turnover <= 2:
    print("コーチ: ナイスゲームや🔥")

elif point >= 10 and turnover <= 5:
    print("コーチ: まぁ次も頑張れ🏀")

elif turnover >= 8:
    print("コーチ: 今すぐ体育館100周や🏃💨")

elif point <= 5:
    print("コーチ: お前今日は何しに来たんや😡")

else:
    print("コーチ: 次はベンチスタートな😤")
