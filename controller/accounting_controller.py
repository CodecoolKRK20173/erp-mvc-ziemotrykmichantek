# everything you'll need is imported:
from view import terminal_view
from model.accounting import accounting
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
               'Show which year has the highest profit',
               'Show the avarage profit in given year for every transaction']

    title_list = ["id", "month", "day", "year", "type", "amount"]
    file_name = 'model/accounting/items.csv'

    common.common_controlls(options, title_list, file_name, accounting)
