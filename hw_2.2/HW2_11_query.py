def field_filter(name: str, values: list):
    """Saves info about fields to filter and its possible values

    :param name: the name of the field we want to filter by
    :type name: str
    :param values: possible values of the considered field
    :type values: list
    :return: None
    """
    to_filter[name] = values


def select(*names: str):
    """Saves info about fields to keep

    :param names: collection of field names we want to keep
    :type names: collection of strings
    :return: None
    """
    selected.extend(names)


def query(friends: list, *args):
    """Filteres friends: keeps only needed fields with needed values

    :param friends: list of dicts
    :param args: anything
    :return: None
    """
    cutted_friends = []
    for friend in friends:
        # match shows if values of all fields of current friend matches
        match = True
        for field in to_filter:
            # friends values should be in values from 'to_filter'
            match = match and friend[field] in to_filter[field]
        if match:
            # keep only needed fields
            cutted_friend = {field: friend[field] for field in selected}
            cutted_friends.append(cutted_friend)
    return cutted_friends


selected = []
to_filter = {}
friends = [
    {'name': 'Сэм', 'gender': 'Мужской', 'sport': 'Баскетбол', 'email': 'email@email.com'},
    {'name': 'Эмили', 'gender': 'Женский', 'sport': 'Волейбол', 'email': 'email1@email1.com'}
]

result = query(
    friends,
    select('name', 'gender', 'sport'),
    field_filter('sport', ['Баскетбол', 'Волейбол']),
    field_filter('gender', ['Мужской'])
)

print(result) # [{'name': 'Сэм', 'gender': 'Мужской', 'sport': 'Баскетбол'}, ​​​​]