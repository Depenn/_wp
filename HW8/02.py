def average(data):
    for student in data:
        score = student['score']
        total = sum(score)
        avg = round(total / len(score), 1)
        print(f"{student['name']}: total = {total}, average = {avg}")
        
students = [
    {'name': 'Graham', 'score': [67, 70, 100]},
    {'name': 'Bell', 'score': [80, 90, 40]},
]

average(students)
