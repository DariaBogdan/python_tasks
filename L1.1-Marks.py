students_count = int(input('Enter the number of students in the course> '))
tasks_count = int(input('Enter the number of tasks in the course> '))
students_names = []
for i in range(students_count):
    students_names.append(input(f"Enter the name of student number {i+1}> "))
students_rating = {}
tasks_rating = {}
for name in students_names:
    for task in range(1, tasks_count+1):
        mark = int(input(f"Enter the student's grade for {name} challenge number {task}> "))
        while mark>10 or mark<0:
            mark = int(input(f"Enter the student's grade for {name} challenge number {task}> "))
        students_rating[name] = students_rating.get(name, 0) + mark
        tasks_rating[task] = tasks_rating.get(task, 0) + mark
print('TOP-3 students: \n', sorted(students_rating, key = lambda x: students_rating[x], reverse=True)[:3])
print('TOP-3 tasks: \n', sorted(tasks_rating, key = lambda x: tasks_rating[x])[:3])