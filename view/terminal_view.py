from view import getch_module

getch = getch_module.instant_input()

""" Terminal view module """

def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your goes code
    titles_char_number = []
    titles_char_number = [0] * len(table[0])
    title_list = [x.upper() for x in title_list]

    table.insert(0, title_list)

    for line in table:
        len_of_longest_string = 0
        for i in range(len(line)):
            if titles_char_number[i] < len(line[i]):
                titles_char_number[i] = len(line[i])

    for i in range(len(table[0])):
        print("+" + "=" * (titles_char_number[i]+4) + "+", end="")
    print("")
    for i in range(len(table[1])):
        print("|{:^{y}}|".format(table[0][i], y=titles_char_number[i] + 4), end="")
    print("")
    for i in range(len(table[0])):
        print("+" + "=" * (titles_char_number[i]+4) + "+", end="")
    print("")

    for j in range(1, len(table)):
        for i in range(len(table[j])):
            print("|{:^{y}}|".format(table[j][i], y=titles_char_number[i] + 4), end="")
        print("")
        for i in range(len(table[j])):
            print("+" + "-" * (titles_char_number[i]+4) + "+", end="")
        print("")

def print_result(result):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    if type(result) is int or type(result) is str or type(result) is float:
        print(type(result))
    elif type(result) is list or type(result) is tuple or type(result) is dict or type(result) is set:
        for i, element in enumerate(result):
            print(str(i+1)+'.', element)
    else:
        print(result)
    print()


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print(title.upper())
    letters_tuple = ("A","B","C","D","E","F","G")
    letters_index = 0
    for id, option in enumerate(list_options):
        if id+1 < 10:
            print('\n     [' + str(id+1) + '] ' + option.upper())
        else:
            print('\n     [' + letters_tuple[letters_index] + '] ' + option.upper())
            letters_index += 1
    print('\n     [0] ' + exit_message.upper())


def get_inputs(list_labels, title):
    inputs = []
    print(title)
    for question in list_labels:
        inputs.append(input(question))

    return inputs

def get_choice():
    print('\nChoose option. ')
    inputs = getch()
    return inputs

def print_error_message(message):
    print('Error: ', message)

def get_record(titles):
    inputs = get_inputs(titles[0],titles[1])
    return inputs

def get_id():
    id = input('Enter ID: ')
    return id

def get_from_to_date():
    print('Enter date')
    needed_inputs = ('From which year: ', 'From which month: ', 'From which day: ', 'To which year: ', 'To which month: ', 'To which day:')
    input_list = []
    for question in needed_inputs:
        input_list.append(input(question))
    return [input_list[1], input_list[2], input_list[0], input_list[4], input_list[5], input_list[3]]

def get_year():
    try:
        year = int(input("What year are you interested in? "))
        return year
    except ValueError:
        print("Wrong input! Use numbers.")

def get_manufacturer():
    manuf = input("What manufacturer are you interested in? ")
    return manuf

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_primitive_logo():
    print(bcolors.OKGREEN+bcolors.BOLD+bcolors.UNDERLINE+"""
    ░/░/░/  ░/      ░/      ░/░/  ░/░/░/            ░/░/░/    ░/      ░/░/░/░/░/░/░/
     ░/    ░/░/    ░/    ░/        ░/    ░/░/░/      ░/    ░/░/░/░/  ░/
    ░/    ░/  ░/  ░/  ░/░/░/░/    ░/    ░/    ░/    ░/      ░/      ░/░/░/░/
   ░/    ░/    ░/░/    ░/        ░/    ░/    ░/    ░/      ░/      ░/
░/░/░/  ░/      ░/    ░/      ░/░/░/  ░/    ░/  ░/░/░/      ░/░/  ░/░/░/░/░/░/░/
Pr0j3ct=
"""+bcolors.ENDC)
