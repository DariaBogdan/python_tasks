#!/usv/bin/env python3.6
def get_top_length():
    """Sets length of top to be shown."""
    return 3


def get_data():
    """Sets data to sort."""
    return [
        {'name': 'Alexey', 'rate': 10, 'course': 'Python'},
        {'name': 'Alexey', 'rate': 3, 'course': 'English'},
        {'name': 'Tom', 'rate': 2, 'course': 'Python'},
        {'name': 'Tom', 'rate': 10, 'course': 'English'},
        {'name': 'Ivan', 'rate': 8, 'course': 'Python'},
        {'name': 'Ivan', 'rate': 1, 'course': 'English'},
        {'name': 'Petr', 'rate': 5, 'course': 'Python'},
        {'name': 'Petr', 'rate': 9, 'course': 'English'}
    ]


def get_courses(data):
    """Returns set of courses from data.

    Note:
        'Noname course' will be used instead course name,
        if field 'course' is not presented.
    """
    assert isinstance(data, list) and all(isinstance(item, dict) for item in data), \
        'in get_courses(data) "data" should be a list of dicts'
    return set(item.get('course', 'Noname course') for item in data)


def get_course_rates(data, course):
    """Returns dict {student: his rate} for the given course.

    Note:
        'Noname student' will be used instead student's name,
            if field 'name' is not presented.
        Value 0 will be used instead student's rate,
            if field 'rate' is not presented.
    """
    assert isinstance(data, list) and all(isinstance(item, dict) for item in data), \
        'in get_course_rates(data, course) "data" should be a list of dicts'
    return {item.get('name', 'Noname Student'): item.get('rate', 0) for item in data if item.get('course') == course}


def show_top_course(course_rates, top_length):
    """Return string containing top_lenght students with greatest rates."""
    assert isinstance(course_rates, dict), '"course_rates" should be dict'
    return ', '.join(sorted(course_rates, key=lambda student: course_rates[student], reverse=True)[: top_length])


if __name__ == '__main__':
    # for every course from data show it's name and top students
    print('\n'.join([f'{course}: {show_top_course(get_course_rates(get_data(), course), get_top_length())}'
                     for course in get_courses(get_data())]))
