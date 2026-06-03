def judge_pg(point, assist, three_rate):

    if assist >= 7 and three_rate >= 40:
        return "プレイメーカーシューター🔥"

    elif assist >= 7:
        return "プレイメーカー🎯"

    elif three_rate >= 40:
        return "シューター🏹"

    elif point >= 20:
        return "スコアラー🔥"

    else:
        return "バランス型🏀"


point = int(input("平均得点: "))
assist = int(input("平均アシスト: "))
three_rate = int(input("3P成功率(%): "))

result = judge_pg(point, assist, three_rate)

print("===== PG診断結果 =====")
print(result)
