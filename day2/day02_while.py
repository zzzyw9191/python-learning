scores = []
while True:
    score_text = input("请输入成绩，输入 q 结束：")
    if score_text == 'q':
        break
    try:
        score = int(score_text)
    except ValueError:
        print("请输入整数成绩")
        continue
    if score < 0 or score > 100:
        print("成绩应在0～100之间")
        continue
    scores.append(score)
print("录入结束")
print(f"所有成绩：{scores}")