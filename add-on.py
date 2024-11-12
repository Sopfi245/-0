grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_1 = list(students)
students_1.sort()
grades_1 = {student: sum(grades) / len(grades)
for student, grades in zip(students_1, grades)}
for student, average in grades_1.items():
    print(f"{student}: {average:.3f}")