game_count = int(input("試合数を入力してください: "))
points = []

for i in range(game_count):
    point = int(input(f"{i + 1}試合目の得点: "))
    points.append(point)

average = sum(points) / len(points)

print("===== 各試合 =====")
for point in points:
    print(f"{point}点")

print("===== シーズン結果 =====")
print(f"総得点: {sum(points)}点")
print(f"平均得点: {average:.1f}点")
print(f"最高得点: {max(points)}点")
print(f"最低得点: {min(points)}点")

if average >= 25:
    print("評価: MVP候補🏆")
elif average >= 20:
    print("評価: オールスター⭐")
elif average >= 15:
    print("評価: スタメン🏀")
else:
    print("評価: ベンチメンバー")
