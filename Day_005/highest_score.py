student_scores = input("Input a list of scores of students separated by space:\n").split(" ")
#student_scores = "1 2 3 4".split(" ")

#highest_score = max(student_scores)

highest_score = 0
for score in student_scores:
    if int(score) > highest_score:
        highest_score = int(score)

print(f"The highest score in the class is: {highest_score}")
