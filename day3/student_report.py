names = ["张三", "李四", "王五", "赵六", "孙七"]
scores = [85, 59, 92, 48, 76]
passed_students = []
failed_students = []
for name,score in zip(names,scores):
    if score >= 60:
        passed_students.append(name)
    else:
        failed_students.append(name)
print(f"及格学生：{passed_students}")
print(f"不及格学生：{failed_students}")