# use map

# syntax map(function, iterable)


# ex1
def add_10(x):
    return x + 10


numbers = [12, 32, 43, 2]

numbers_10 = map(add_10, numbers)
print(type(numbers_10))
# print(*numbers_10)
for num in numbers_10:
    print(num)

# use filter
# syntaxt filter(function, iterable) # function that returns true or false

# we want to get numbers that are even


def is_even(x):
    return True if x % 2 == 0 else False

even_numbers_10 = filter(is_even, numbers)
print(*even_numbers_10)




students = {
    'student_01_RW': {
        'name': 'Manzi Omar',
        'age': 20,
        'sex': 'Male',
        'nationality': 'Rwandan'
    },
    'student_02_RW': {
        'name': 'Keza Kamali',
        'age': 21,
        'sex': 'Female',
        'nationality': 'Rwandan'
    },
    'student_03': {
        'name': 'Levis Iradukunda',
        'age': 23,
        'sex': 'Male',
        'nationality': 'Tanzanian'
    },
    'student_04': {
        'name': 'Max obiku',
        'age': 24,
        'sex': 'Male',
        'nationality': 'Kenyan'
    }

}


rw_students = {key: value for key, value in students.items() if key.endswith('RW')}
print(rw_students)


class First:
    ...

classes = [First]
print(First.__class__.__name__)