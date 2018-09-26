# everything you'll need is imported:
from view import terminal_view
from model.hr import hr
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
               'Show oldest person',
               'Show closest person to avarage age in data']

    title_list = ["id", "name", "birth_year"]
    table = data_manager.get_table_from_file('model/hr/persons.csv')

    terminal_view.print_menu("Choose option:",options,"Back to main menu")
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice()
        common.clear_function()
        if choice == "1":
            hr.add(data_manager.get_table_from_file('model/hr/persons.csv', terminal_view.get_record() ))
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "2":
            terminal_view.print_table(table, title_list)
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "3":
            hr.update(data_manager.get_table_from_file('model/hr/persons.csv', terminal_view.get_id() ))
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "4":
            hr.remove(data_manager.get_table_from_file('model/hr/persons.csv', terminal_view.get_id() ))
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        else:
            terminal_view.print_error_message("There is no such choice.")
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
