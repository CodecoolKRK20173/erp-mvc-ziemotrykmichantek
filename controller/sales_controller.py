# everything you'll need is imported:
from view import terminal_view
from model.sales import sales
from controller import common

def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    # your code
    common.common_controller(sales.add(get_table_from_file('sales.csv', terminal_view.get_record() )),
    sales.run(get_table_from_file('sales.csv')),
    sales.update(get_table_from_file('sales.csv', terminal_view.get_id() )),
    sales.remove(get_table_from_file('sales.csv', terminal_view.get_id() )) )
