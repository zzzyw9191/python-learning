# 学生成绩管理：字典综合练习

# 1. 使用 zip() 和 dict() 创建课程成绩字典
courses = ["Python", "数学", "英语"]
scores = [93, 88, 91]

grades = dict(zip(courses, scores))
print("原始成绩：", grades)

# 2. 安全查询成绩：课程不存在时返回默认值
print("物理成绩：", grades.get("物理", "未录入"))

# 3. 批量更新成绩：修改已有课程，添加新课程
updates = {"Python": 96, "物理": 89}
grades.update(updates)

print("更新成绩：", grades)

# 4. 遍历字典，输出课程名称与对应成绩
for course, score in grades.items():
    print(f"{course}：{score}")

