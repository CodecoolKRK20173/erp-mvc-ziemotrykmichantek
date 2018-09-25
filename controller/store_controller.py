# everything you'll need is imported:
from model.store import store
from view import terminal_view
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
    common.common_controller(store.add(get_table_from_file('games.csv', terminal_view.get_record() )),
    store.run(get_table_from_file('games.csv')),
    store.update(get_table_from_file('games.csv', terminal_view.get_id() )),
    store.remove(get_table_from_file('games.csv', terminal_view.get_id() )) )
