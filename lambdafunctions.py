students = [('Alice', 88), ('Bob', 72), ('Charlie', 95)]
sorted_students = sorted(students, key=lambda s: s[1], reverse=False)
print(sorted_students)