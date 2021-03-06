""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""

# everything you'll need is imported:
from model import common
from view import terminal_view



def add(table, record):
    """
    Add new record to table

    Args:
        table (list): table to add new record to
        record (list): new record

    Returns:
        list: Table with a new record
    """
    # your code
    return common.common_add(table, record)


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code
    return common.common_remove(table, id_)


def update(table, id_, record):
    """
    Updates specified record in the table.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update
        record (list): updated record

    Returns:
        list: table with updated record
    """

    # your code
    return common.common_update(table, id_, record)


# special functions:
# ------------------
def special_function(table):
    return get_oldest_person(table)

def special_function2(table):
    return get_persons_closest_to_average(table)

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    #your code
    for i, record in enumerate(table):
        if i==0:
            oldest_person = record
        if int(oldest_person[2]) > int(record[2]):
            oldest_person = record
    oldest_persons = [oldest_person[1]]
    for i, record in enumerate(table):
        if int(record[2])==int(oldest_person[2]):
            if oldest_person[1]!=record[1]:
                oldest_persons.append(record[1])
    return oldest_persons

def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    # your code
    list_of_birth_years = [int(person[2]) for person in table]
    average_birth_year = sum(list_of_birth_years) / len(list_of_birth_years)
    for i, person in enumerate(table):
        current_name = person[1]
        current_year = int(person[2])
        range_from_year_to_average = abs(average_birth_year - current_year)
        if i == 0:
            name_closest_to_average = current_name
            year_closest_to_average = current_year
            smallest_range_to_average = range_from_year_to_average
            continue
        if range_from_year_to_average < smallest_range_to_average:
            name_closest_to_average = current_name
            year_closest_to_average = current_year
            smallest_range_to_average = range_from_year_to_average
    list_of_names_closest_to_average = [name_closest_to_average]
    for person in table:
        current_name = person[1]
        current_year = int(person[2])
        if current_year == year_closest_to_average and current_name not in list_of_names_closest_to_average:
            list_of_names_closest_to_average.append(current_name)
    return list_of_names_closest_to_average
