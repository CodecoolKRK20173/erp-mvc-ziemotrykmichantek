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


def get_title_by_id_from_table(table, id):

    """
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the sales table
        id (str): the id of the item

    Returns:
        str: the title of the item
    """

    # your code
    for line in table:
        if line[0] == id:
            return line[2]
    return "No such ID"


def get_item_id_or_title_sold_last_from_table(table, id_or_title):
    """
    Returns the _id_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    # your code
    print(table)
    for i, line in enumerate(table):
        current_date_int = int(line[6]) + int(line[4]) + int(line[5])
        current_id_and_title = (line[0], line[2])
        if i == 0:
            last_sold_date = current_date_int
            last_title_id_and_name = current_id_and_title
            continue
        if current_date_int > last_sold_date:
            last_sold_date = current_date_int
            last_title_id_and_name = current_id_and_title
    if id_or_title:
        return last_title_id_and_name[2]
    else:
        return last_title_id_and_name[0]


def get_the_sum_of_prices_from_table(table):
    """
    Returns the sum of the prices of the items in the item_ids.

    Args:
        table (list of lists): the sales table

    Returns:
        number: the sum of the items' prices
    """

    # your code
    return sum(list(map(lambda element: int(element[3]), table)))


def get_customer_id_by_sale_id_from_table(table, sale_id):
    """
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
        table: table to remove a record from
        sale_id (str): sale id to search for
    Returns:
        str: customer_id that belongs to the given sale id
    """
    # your code
    for line in table:
        if sale_id == line[7]:
            return line[0]
    return 'No such ID'


def get_all_customer_ids_from_table(table):
    """
    Returns a set of customer_ids that are present in the table.

    Args:
        table (list of list): the sales table
    Returns:
         set of str: set of customer_ids that are present in the table
    """

    # your code
    return set(map(lambda element: element[0], table))


def get_all_sales_ids_for_customer_ids_from_table(table):
    """
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Args:
        table (list of list): the sales table
    Returns:
         (dict of (key, value): {customer_id: (list) sale_ids}) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """

    # your code
    customer_and_sales_ids = {}
    for line in table:
        customer_id = line[0]
        sales_id = line[7]
        if customer_id not in customer_and_sales_ids:
            customer_and_sales_ids[customer_id] = [sales_id]
        else:
            customer_and_sales_ids[customer_id].append(sales_id)
    return customer_and_sales_ids

def get_num_of_sales_per_customer_ids_from_table(table, customer_id):
    """
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Args:
        table (list of list): the sales table
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code
    customer_and_number_of_sales = {}
    for line in table:
        customer_id = line[0]
        if customer_id not in customer_and_number_of_sales:
            customer_and_number_of_sales[customer_id] = 1
        else:
            customer_and_number_of_sales[customer_id] += 1
    return customer_and_number_of_sales
