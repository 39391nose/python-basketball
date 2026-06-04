game_count = int(input("試合数を入力してください: "))

points = []

for i in range(game_count):
    point = int(input(f"{i + 1}試合目の得点: "))
    points.append(point)

average = sum(points) / len(points)

print("===== シーズン結果 =====")
print(f"総得点: {sum(points)}点")
print(f"平均得点: {average:.1f}点")
print(f"最高得点: {max(points)}点")
print(f"最低得点: {min(points)}点")
