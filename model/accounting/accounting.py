""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
"""

# everything you'll need is imported:
from model import data_manager
from model import common



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
    return which_year_max(table)

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """

    # your code
    years_and_profit_dict = {}
    for i, record in enumerate(table):
        year = record[3]
        profit_or_not_profit_absolute_value = int(record[5])
        if year not in years_and_profit_dict:
            if record[4] == 'in':
                years_and_profit_dict[year] = int(profit_or_not_profit_absolute_value)
            else:
                years_and_profit_dict[year] = -int(profit_or_not_profit_absolute_value)
        else:
            if record[4] == 'in':
                years_and_profit_dict[year] += int(profit_or_not_profit_absolute_value)
            else:
                years_and_profit_dict[year] -= int(profit_or_not_profit_absolute_value)
    return int(max(years_and_profit_dict, key = years_and_profit_dict.get))

def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    # your code
    profit = 0
    for i, record in enumerate(table):
        current_year = int(record[3])
        if current_year == year:
            if record[4] == 'in':
                profit += int(record[5])
            else:
                profit -= int(record[5])
        if i == len(table)-1:
            number_of_transactions = i
    return profit/number_of_transactions
