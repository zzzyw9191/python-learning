import copy
students = {
    "张三": {
        "scores": [80, 90]
    },
    "李四": {
        "scores": [70, 85]
    }
}

copied_students = copy.deepcopy(students)
copied_students["张三"]["scores"].append(100)

print(f"原数据：{students}")
print(f"复制数据：{copied_students}")