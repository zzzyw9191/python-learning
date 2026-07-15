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

if not scores:
    print("没有录入任何成绩")
else:
    total = 0
    count = 0
    highest = scores[0]
    lowest = scores[0]
    print(f"所有成绩：{scores}")
    for score in scores:
        total = total + score
        if score > highest:
            highest = score
        if score < lowest:
            lowest = score
        if score >= 60:
            count = count + 1
    average = total / len(scores)
    print(f"平均分：{average:.1f}")
    print(f"及格人数：{count}")
    print(f"最高分：{highest}")
    print(f"最低分：{lowest}")