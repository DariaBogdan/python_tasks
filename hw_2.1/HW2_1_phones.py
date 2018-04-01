def add(d: dict) -> None:
    """
    Adds new records to the phonebook.

    :param d: dict to add item in
    :type d: dict
    :return: None
    :raises: nothing
    """
    name = input('Input name to add> ').title()
    d[name] = d.get(name, []) + [input('Input the phone> ')]


def show(d: dict) -> None:
    """
    Shows all records from the phonebook by name, if exist.

    :param d: dict to show item from
    :type d: dict
    :return: None
    :raises: nothing
    """
    name = input('Input name to show> ').title()
    if name in d:
        print('name     phone')
        for phone in d[name]:
            print(name, phone)
    else:
        print(f'There is no records for {name}.')


def delete(d: dict) -> None:
    """
    Delete records from phonebook by name, if exist.
    :param d: dict to delete item from
    :type d: dict
    :return: None
    :raises: nothing
    """
    name = input('Input name to delete> ').title()
    if name in d:
        del d[name]
    else:
        print(f'There is no records for {name}.')


phone_dict = {}
while True:
    action = input('This programm imitates telephone directory.\n'
                   'What can this programm do?\n'
                   '-- to add phone number and name type "add"\n'
                   '-- to show phone number by name type "show"\n'
                   '-- to delete records by name type "delete"\n'
                   '-- to exit type "exit"\n'
                   'Type what you want to do> ')
    while action not in ['add', 'show', 'delete', 'exit']:
        action = input('Incorrect input! Choose one of the following:\n'
                       '-- to add phone number and name type "add"\n'
                       '-- to show phone number by name type "show"\n'
                       '-- to delete records by name type "delete"\n'
                       '-- to exit type "exit"\n'
                       'Type what you want to do> ')

    if action == 'add':
        add(phone_dict)
    elif action == 'show':
        show(phone_dict)
    elif action == 'delete':
        delete(phone_dict)
    elif action == 'exit':
        break