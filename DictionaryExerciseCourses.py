CourseInformation = {
    'CS101': {
        'Room Number': '3004',
        'Instructor': 'Haynes',
        'Meeting Time': '8:00 a.m.'

    },
    'CS102': {
        'Room Number': '4501',
        'Instructor': 'Alvarado',
        'Meeting Time': '9:00 a.m.'
    },
    'CS103': {
        'Room Number': '6755',
        'Instructor': 'Rich',
        'Meeting Time': '10:00 a.m.'
    },
    'NT110': {
        'Room Number': '1244',
        'Instructor': 'Burke',
        'Meeting Time': '11:00 a.m.'
    },
    'CM241': {
        'Room Number': '1411',
        'Instructor': 'Lee',
        'Meeting Time': '1:00 p.m.'
    }
}
print()
print()
course_num = input('What course number are you inquiring about?  ')
print()

print('Course Number: ', course_num)
print('Room Number: ', CourseInformation[course_num]['Room Number'])
print('Instructor: ', CourseInformation[course_num]['Instructor'])
print('Meeting Time: ', CourseInformation[course_num]['Meeting Time'])

print()






