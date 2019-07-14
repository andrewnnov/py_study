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


def add_mark(student, mark):
    # Append a mark to the student dictionary
    student['marks'].append(mark)


def calculate_average_mark(student):
    # add together all of student[marks']

    # divide them by the total number of marks
    number = len(student['marks'])
    if number == 0:
        return 0

    total = sum(student['marks'])
    return total / number


s = create_student()

add_mark(s, 5)
add_mark(s, 3)

print(calculate_average_mark(s))

