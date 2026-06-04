points = [20, 15, 27, 18, 31]

print("===== シーズン成績 =====")

for point in points:
    print(f"{point}点")

average = sum(points) / len(points)

print("----------------")
print(f"平均得点: {average:.1f}点")
print(f"最高得点: {max(points)}点")
print(f"最低得点: {min(points)}点")

