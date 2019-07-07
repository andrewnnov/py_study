student = {"name": "Jose",
           "mark": [20, 40, 70, 80, 99],
           "exams": {
               "final": 70,
               "midterm": 50
           }}

print(student['exams']['final'])


def create_student():
    # ask the user for the student's name
    # Create the dictionary in the format {'name': '<student_name>, 'marks': []}
    # return that dictionary
    name = input("Please enter the new student's name: ")
    student_data = {
        'name': name,
        'marks': []
    }
    return student_data


print(create_student())

