""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
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
    return get_counts_by_manufacturers(table)

def special_function2(table):
    manufacturer = terminal_view.get_manufacturer()
    return get_average_by_manufacturer(table, manufacturer)


def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    # your code
    dict = {}
    for record in table:
        if record[2] in dict:
            dict[record[2]]+= 1
        else:
            dict[record[2]]= 1
    return dict

def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    # your code
    in_stock_list = []
    for record in table:
        if record[2] == manufacturer:
            in_stock_list.append(int(record[4]))
    if len(in_stock_list) == 0:
        in_stock_list.append(0)
    return sum(in_stock_list)/len(in_stock_list)
