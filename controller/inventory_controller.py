# everything you'll need is imported:
from view import terminal_view
from model.inventory import inventory
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
               'Show which items have not exceeded their durability',
               'Show avarage durability time for each manufacturer']

    title_list = ["id", "name", "manufacturer", "purchase_year", "durability"]
    file_name = 'model/inventory/inventory.csv'

    common.common_controlls(options, title_list, file_name, inventory)
