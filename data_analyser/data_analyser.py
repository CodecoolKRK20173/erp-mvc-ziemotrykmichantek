""" Data analyser module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * customer
    * tittle of game
    * price
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
"""
"""
This module creates reports for the marketing department.
This module can run independently from other modules.
Has no own data structure but uses other modules.
Avoud using the database (ie. .csv files) of other modules directly.
Use the functions of the modules instead.
"""

# todo: importing everything you need

# importing everything you need
import view
from model import common
from model import sales
from model import crm


def get_the_last_buyer_name_or_id(table, id_or_name):
    """
    Returns the customer _name_ of the customer made sale last.

    Returns:
        str: Customer name of the last buyer
    """

    # your code
    for i, line in enumerate(table):
        current_date_int = int(line[6]) + int(line[4]) + int(line[5])
        current_id_and_name = (line[0], line[1])
        if i == 0:
            last_bought_date = current_date_int
            last_customer_id_and_name = current_id_and_name
            continue
        if current_date_int > last_bought_date:
            last_bought_date = current_date_int
            last_customer_id_and_name = current_id_and_name
    if id_or_name:
        return last_customer_id_and_name[1]
    else:
        return last_customer_id_and_name[0]


def get_customer_money_spent_id_or_name(table, id_or_name):
    """
    Returns the customer's _name_ who spent the most in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer name and the sum the customer spent eg.: ('Daniele Coach', 42)
    """

    # your code
    names_and_money_spent_dict = {}
    for line in table:
        current_id = line[0]
        current_name = line[1]
        current_money = line[3]
        current_id_and_name = current_id + '|' + current_name
        if current_id_and_name not in names_and_money_spent_dict:
            names_and_money_spent_dict[current_id_and_name] = current_money
        else:
            names_and_money_spent_dict[current_id_and_name] += current_money
    most_money_spent_id_and_name = max(names_and_money_spent_dict, key=names_and_money_spent_dict.get)
    most_money_spent_id_and_name = most_money_spent_id_and_name.split("|")
    most_money_spent_id = most_money_spent_id_and_name[0]
    most_money_spent_name = most_money_spent_id_and_name[1]
    if id_or_name:
        return most_money_spent_name
    else:
        return most_money_spent_id

def get_the_most_frequent_buyers_id_or_name(table, id_or_name, num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer's name) who bought most frequently in an
    ordered list of tuples of customer names and the number of their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer names and num of sales
            The first one bought the most frequent. eg.: [('Genoveva Dingess', 8), ('Missy Stoney', 3)]
    """

    # your code
    names_and_buy_frequency_dict = {}
    for line in table:
        current_id = line[0]
        current_name = line[1]
        current_id_and_name = current_id + '|' + current_name
        if current_id_and_name not in names_and_buy_frequency_dict:
            names_and_buy_frequency_dict[current_id_and_name] = 1
        else:
            names_and_buy_frequency_dict[current_id_and_name] += 1
    most_frequent_buyer_id_and_name = max(names_and_buy_frequency_dict, key=names_and_buy_frequency_dict.get)
    most_frequent_buyer_id_and_name = most_frequent_buyer_id_and_name.split("|")
    most_frequent_buyer_id = most_frequent_buyer_id_and_name[0]
    most_frequent_buyer_name = most_frequent_buyer_id_and_name[1]
    if id_or_name:
        return most_frequent_buyer_name
    else:
        return most_frequent_buyer_id
