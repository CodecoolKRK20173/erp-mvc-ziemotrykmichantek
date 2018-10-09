""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
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
    return get_lowest_price_item_id(table)

def special_function2(table):
    dates = terminal_view.get_from_to_date()
    return get_items_sold_between(table, dates[0], dates[1], dates[2], dates[3], dates[4], dates[5])

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    # your code

    for i, record in enumerate(table):
        if i == 0:
            lowest_prize = int(record[2])
            lowest_prize_id = record[0]
        if int(record[2]) < lowest_prize:
            lowest_prize = int(record[2])
            lowest_prize_id = record[0]
    for i, record in enumerate(table):
        if int(record[2]) == lowest_prize:
            lowest_prize_id = common.return_the_last_item_by_alphabetical_order_of_the_title(table)
    return lowest_prize_id



def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    # your code
    list_of_items=[]
    month_from, day_from, year_from, month_to, day_to, year_to = int(month_from), int(day_from), int(year_from), int(month_to), int(day_to), int(year_to)
    for i, record in enumerate(table):
        record_month = int(record[3])
        record_day = int(record[4])
        record_year = int(record[5])
        if year_from < record_year < year_to:
            list_of_items.append(record)
        elif year_from == record_year or year_to == record_year:
            if month_from < record_month < month_to:
                list_of_items.append(record)
            elif month_from == record_month or month_to == record_month:
                if day_from < record_day < day_to:
                    list_of_items.append(record)
                elif day_from == record_day or day_to == record_day:
                    list_of_items.append(record)
    return list_of_items
