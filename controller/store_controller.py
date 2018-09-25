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

    terminal_view.print_menu("Choose option:",options,"Back to main menu")
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice()
        if choice == "1":
            data_manager.write_table_to_file('model/store/games.csv',store.add(data_manager.get_table_from_file('model/store/games.csv'), terminal_view.get_record() ))
        elif choice == "2":
            terminal_view.print_table(data_manager.get_table_from_file('model/store/games.csv'))
        elif choice == "3":
            store.update(data_manager.get_table_from_file('model/store/games.csv'), terminal_view.get_id() )
        elif choice == "4":
            store.remove(data_manager.get_table_from_file('model/store/games.csv'), terminal_view.get_id() )
        else:
            terminal_view.print_error_message("There is no such choice.")
