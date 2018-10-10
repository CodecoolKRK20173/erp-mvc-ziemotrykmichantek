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
    options = ['Create',
               'Read',
               'Update',
               'Delete',
               'Show the id of the customer with the longest name',
               'Show which customer has subcribed to the newsletter',
               'Show customer\'s name by ID']

    get_record_data = (['Name: ', 'Email: ', 'Subscribed: '], 'New person:')
    title_list = ["id", "name", "email", "subscribed"]
    file_name = 'model/crm/customers.csv'

    common.common_controlls(options, title_list, file_name, crm, get_record_data, False)
