# everything you'll need is imported:
from view import terminal_view
from model.sales import sales
from controller import common
from model import data_manager

def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    # your code
    options = ['Create',
               'Read',
               'Update',
               'Delete',
               'Show lowest prize item id',
               'Show items sold between given dates',
               'Show title by ID',
               'Show ID of the last sold item',
               'Show the sum of all item\'s prizes',
               'Show customer ID by sale ID',
               'Show all customer\'s ID',
               'Show all sales ID\'s',
               'Show number of sales per customer']

    get_record_data = (['Title: ', 'Price: ', 'Month: ', 'Day: ', 'Year'], 'New title')
    title_list = ["id", "title", "price", "month", "day", "year"]
    file_name = 'model/sales/sales.csv'

    common.common_controlls(options, title_list, file_name, sales, get_record_data, True)
