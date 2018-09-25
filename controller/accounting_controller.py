# everything you'll need is imported:
from view import terminal_view
from model.accounting import accounting
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
    common.common_controller(accounting.add(get_table_from_file('items.csv', terminal_view.get_record() )),
    accounting.run(get_table_from_file('items.csv')),
    accounting.update(get_table_from_file('items.csv', terminal_view.get_id() )),
    accounting.remove(get_table_from_file('items.csv', terminal_view.get_id() )) )
