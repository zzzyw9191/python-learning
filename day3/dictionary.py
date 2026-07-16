scores = {
    "张三": 85,
    "李四": 59,
    "王五": 92,
    "赵六": 48
}
scores["李四"] = 65
scores["孙七"] = 76
count = 0
for name,score in scores.items():
    print(f"{name}: {score}分")
    if score >= 60:
        count += 1
print(f"及格人数：{count}")
print(f"查询结果：{scores.get("周八","未找到该学生")}")
