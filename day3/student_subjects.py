students = {
    "张三": {
        "math": 85,
        "english": 78
    },
    "李四": {
        "math": 59,
        "english": 88
    },
    "王五": {
        "math": 92,
        "english": 95
    }
}
def analyze_scores(math_score, english_score, pass_score=60):
    average_score = (math_score + english_score) / 2

    if average_score >= pass_score:
        result = "及格"
    else:
        result = "不及格"

    return average_score, result
students["张三"]["physics"] = 90
students["李四"]["math"] = 65
for name, information in students.items():
    math_score = information["math"]
    english_score = information["english"]
    average_score, result = analyze_scores(
        math_score=math_score,
        english_score=english_score
    )
    print(
    f"{name}：数学{math_score}分，"
    f"英语{english_score}分，"
    f"平均分{average_score:.1f},{result}"
)
average_score, result = analyze_scores(
    math_score=70,
    english_score=80,
    pass_score=80
)

print(f"测试结果：平均分{average_score:.1f},{result}")
