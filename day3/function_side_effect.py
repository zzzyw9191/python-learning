def add_score_in_place(scores, score):
    scores.append(score)
def add_score_safely(scores, score):
    new_scores = scores.copy()
    new_scores.append(score)
    return new_scores
original_scores = [80, 90]

add_score_in_place(original_scores, 70)
print(f"第一次修改后：{original_scores}")

new_scores = add_score_safely(original_scores, 100)
print(f"原列表：{original_scores}")
print(f"新列表：{new_scores}")