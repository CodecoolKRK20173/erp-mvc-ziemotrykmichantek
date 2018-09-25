# everything you'll need is imported:
from view import terminal_view
from model.hr import hr
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
    common.common_controller(hr.add(get_table_from_file('persons.csv', terminal_view.get_record() )),
    hr.run(get_table_from_file('persons.csv')),
    hr.update(get_table_from_file('persons.csv', terminal_view.get_id() )),
    hr.remove(get_table_from_file('persons.csv', terminal_view.get_id() )) )
