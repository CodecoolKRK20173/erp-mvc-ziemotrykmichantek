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
    common.common_controller(accounting.add(data_manager.get_table_from_file('items.csv', terminal_view.get_record() )),
    accounting.run(data_manager.get_table_from_file('items.csv')),
    accounting.update(data_manager.get_table_from_file('items.csv', terminal_view.get_id() )),
    accounting.remove(data_manager.get_table_from_file('items.csv', terminal_view.get_id() )) )
