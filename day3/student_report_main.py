from score_utils import analyze_scores
students = {
    "张三": {"math": 85, "english": 78},
    "李四": {"math": 65, "english": 88},
    "王五": {"math": 92, "english": 95}
}
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