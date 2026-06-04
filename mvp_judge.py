points = [20, 15, 27, 18, 31]

average = sum(points) / len(points)

print(f"平均得点: {average:.1f}点")

if average >= 25:
    print("MVP候補🏆")
elif average >= 20:
    print("オールスター⭐")
else:
    print("ロールプレイヤー🏀")

