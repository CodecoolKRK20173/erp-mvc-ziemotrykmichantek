# everything you'll need is imported:
from view import terminal_view
from model.crm import crm
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
    common.common_controller(crm.add(data_manager.get_table_from_file('customers.csv', terminal_view.get_record() )),
    crm.run(data_manager.get_table_from_file('customers.csv')),
    crm.update(data_manager.get_table_from_file('customers.csv', terminal_view.get_id() )),
    crm.remove(data_manager.get_table_from_file('customers.csv', terminal_view.get_id() )) )
