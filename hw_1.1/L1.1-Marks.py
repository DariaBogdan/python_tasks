# read the number of students
students_count = input('Enter the number of students in the course> ')
while not students_count.isdigit():
    students_count = input('Enter the number of students in the course (integer)> ')
students_count = int(students_count)

# read the number of tasks
tasks_count = input('Enter the number of tasks in the course> ')
while not tasks_count.isdigit():
    tasks_count = input('Enter the number of tasks in the course (integer)> ')
tasks_count = int(students_count)

# read names
students_names = []
for i in range(students_count):
    students_names.append(input(f"Enter the name of student number {i+1}> "))

# read marks and write them to two dicts
students_rating = {}
tasks_rating = {}
for name in students_names:
    for task in range(1, tasks_count+1):
        mark = input(f"Enter the student's grade for {name} challenge number {task}> ")
        while not mark.isdigit() or (len(mark)>1 and mark != '10'):
            mark = input(f"Enter the student's grade (integer from 0 to 10) for {name} challenge number {task}> ")
        students_rating[name] = students_rating.get(name, 0) + int(mark)
        tasks_rating[task] = tasks_rating.get(task, 0) + int(mark)
# result
print('TOP-3 students: \n', sorted(students_rating, key = lambda x: students_rating[x], reverse=True)[:3])
print('TOP-3 tasks: \n', sorted(tasks_rating, key = lambda x: tasks_rating[x])[:3])