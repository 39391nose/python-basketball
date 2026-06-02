two_attempt = int(input("2P試投数：　"))
two_made = int(input("2P成功数: "))

three_attempt = int(input("3P試投数：　"))
three_made = int(input("3P成功数：　"))

free_throw = int(input("FT成功数：　"))

score = two_made * 2 +three_made * 3 + free_throw
fg_rate = (two_made + three_made) / (two_attempt) * 100
three_rate = three_made / three_attempt * 100

print(f"総得点は｛score｝点です")
print(f"FG成功率は｛fg_rate:.1f｝％です")
print(f"3P成功率は｛three_rate:.1f｝％です")

if score  >= 20:
    print("エース級")
elif score >= 10:
    print("戦力")
else:
    print("もっと打とう") 
           
