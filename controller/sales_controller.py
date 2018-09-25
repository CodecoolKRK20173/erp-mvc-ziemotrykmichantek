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
    common.common_controller(sales.add,
    sales.run,
    sales.update,
    sales.remove, (data_manager.get_table_from_file('model/sales/sales.csv', terminal_view.get_id() )) )
