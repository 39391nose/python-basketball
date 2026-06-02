two_point = int(input("2P成功数："))
three_point = int(input("3P成功数："))
free_throw = int(input("FT成功数: "))

score = two_point * 2 + three_point * 3 + free_throw

print(f"総得点は{score}点です")
