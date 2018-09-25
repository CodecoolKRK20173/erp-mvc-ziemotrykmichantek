# everything you'll need is imported:
from view import terminal_view
from model.inventory import inventory
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
    common.common_controller(inventory.add(get_table_from_file('inventory.csv', terminal_view.get_record() )),
    inventory.run(get_table_from_file('inventory.csv')),
    inventory.update(get_table_from_file('inventory.csv', terminal_view.get_id() )),
    inventory.remove(get_table_from_file('inventory.csv', terminal_view.get_id() )) )
