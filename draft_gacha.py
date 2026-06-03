import random

shoot = random.randint(60, 99)
pass_skill = random.randint(60, 99)
handling = random.randint(60, 99)

ovr = (shoot + pass_skill + handling) // 3

print("===== Draft Result =====")
print(f"OVR {ovr}")
print(f"シュート {shoot}")
print(f"パス {pass_skill}")
print(f"ハンドリング {handling}")

if shoot >= 90:
    print("コンプ: コン・カニップル")
elif pass_skill >= 90:
    print("コンプ: クリス・ポール")
elif handling >= 90:
    print("コンプ: カイリー・アービング")
else:
    print("コンプ: ロールプレイヤー")
