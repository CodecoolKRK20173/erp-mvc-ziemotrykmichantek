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
               'Delete',
               'Check how many different kinds of games in data',
               'Check avarage amount of games in stock of given manufacturer in data']

    title_list = ["id", "title", "manufacturer", "price", "in_stock"]
    file_name = 'model/store/games.csv'

    common.common_controlls(options, title_list, file_name, store)
