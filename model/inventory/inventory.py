""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
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
    return get_available_items(table)

def special_function2(table):
    return get_average_durability_by_manufacturers(table)

def get_available_items(table):
    """
    Question: Which items have not exceeded their durability yet?

    Args:
        table (list): data table to work on

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    # your code
    for i in table:
        list_of_not_exceeded_items = []
        if int(i[3])+int(i[4]) >= 2016: # repository creation date
            list_of_not_exceeded_items.append(table)
        return list_of_not_exceeded_items

def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    # your code
    dict_durability_sum = {}
    dict_how_many = {}
    for i, record in enumerate(table):
        manufacturer = record[2]
        durability = int(record[4])
        if manufacturer not in dict_durability_sum and manufacturer not in dict_how_many:
            dict_durability_sum[manufacturer] = durability
            dict_how_many[manufacturer] = 1
        else:
            dict_durability_sum[manufacturer] += durability
            dict_how_many[manufacturer] += 1

    dict_avarage_durability = {}
    for key in dict_durability_sum:
        dict_avarage_durability[key] = dict_durability_sum[key]/dict_how_many[key]
    return dict_avarage_durability
