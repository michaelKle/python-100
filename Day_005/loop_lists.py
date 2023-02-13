student_heights = input("Input a list of heights of students separated by space:\n").split(" ")
#student_heights = "1 2 3 4".split(" ")

for i in range(0, len(student_heights)):
    student_heights[i] = int(student_heights[i])

print(student_heights)

# sum(student_heights) / len(student_heights)

sum = 0
num = 0
for h in student_heights:
    sum += h
    num += 1

print(f"Average height is {sum / num}")
