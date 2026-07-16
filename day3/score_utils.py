def analyze_scores(math_score, english_score, pass_score=60):
    average_score = (math_score + english_score) / 2

    if average_score >= pass_score:
        result = "及格"
    else:
        result = "不及格"

    return average_score, result