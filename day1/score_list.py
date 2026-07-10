score_texts = input("Enter the scores separated by spaces: ").split()

scores = []

for score_text in score_texts:
    score = float(score_text)
    scores.append(score)

print(f"成绩列表： {scores}")

total = 0
pass_count = 0
highest = scores[0]
lowest = scores[0]
excellent_count = 0
good_count = 0
pass_level_count = 0
fail_level_count = 0
for score in scores:
    total = total + score
    if score >= 60:
        pass_count = pass_count + 1
    if score > highest:
        highest = score
    if score < lowest:
        lowest = score
        
    if score >=90:
        excellent_count = excellent_count + 1
    elif score >= 80:
        good_count = good_count + 1
    elif score >=60:
        pass_level_count = pass_level_count + 1
    else:
        fail_level_count = fail_level_count + 1
average = total / len(scores)
fail_count = len(scores) - pass_count
print(f"总分： {total}")
print(f"平均分： {average:.2f}")
print(f"优秀人数： {excellent_count}")
print(f"良好人数： {good_count}")
print(f"及格人数： {pass_level_count}")
print(f"不及格人数： {fail_level_count}")
print(f"最高分：{highest:.2f}")
print(f"最低分：{lowest:.2f}")

