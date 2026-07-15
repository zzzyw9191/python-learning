scores = [85, 72, 59, 91, 66]
for number, score in enumerate(scores, start=1):
    print(f"第{number}个成绩：{score}")
for index in range(len(scores)-1,-1,-1):
    print(f"第{index + 1}个成绩：{scores[index]}") 