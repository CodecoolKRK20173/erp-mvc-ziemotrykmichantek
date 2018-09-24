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
    options = ['Create',
               'Read',
               'Update',
               'Delete']

    terminal_view.print_menu(options,"Back to main menu")
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(options)
        if choice == "1":
            store.add(get_table_from_file('games.csv', terminal_view.get_record() ))
        elif choice == "2":
            store.run(get_table_from_file('games.csv'))
        elif choice == "3":
            store.update(get_table_from_file('games.csv', terminal_view.get_id() ))
        elif choice == "4":
            store.remove(get_table_from_file('games.csv', terminal_view.get_id() ))
        else:
            terminal_view.print_error_message("There is no such choice.")
