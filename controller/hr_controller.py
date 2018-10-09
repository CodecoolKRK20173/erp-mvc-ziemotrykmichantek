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

    get_record_data = (['Person name: ', 'Birth year: '], 'New Person:')
    title_list = ["id", "name", "birth_year"]
    file_name = 'model/hr/persons.csv'

    common.common_controlls(options, title_list, file_name, hr, get_record_data)
