score_texts = input("请输入成绩，用空格隔开：").split()
scores = []
for score_text in score_texts:
    score = int(score_text)
    scores.append(score)
sum = 0
count = 0
highest = scores[0]
lowest = scores[0]
print(f"所有成绩：{scores}")
for score in scores:
    sum = sum + score
    if score > highest:
        highest = score
    if score < lowest:
        lowest = score
    if score >= 60:
        count = count + 1
average = sum / len(scores)
print(f"平均分：{average:.1f}")
print(f"及格人数：{count}")
print(f"最高分：{highest}")
print(f"最低分：{lowest}")