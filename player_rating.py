point = int(input("平均得点: "))
assist = int(input("平均アシスト: "))
three_rate = int(input("3P成功率(%): "))

shoot = three_rate * 2
pass_skill = assist * 10
handling = point * 3

ovr = (shoot + pass_skill + handling) // 3

print("===== Player Card =====")
print(f"OVR {ovr}")
print(f"シュート {shoot}")
print(f"パス {pass_skill}")
print(f"ハンドリング {handling}")

if three_rate >= 40:
    print("タイプ: シューター🔥")
elif assist >= 5:
    print("タイプ: プレイメーカー🎯")
else:
    print("タイプ: スコアラー🏀")
