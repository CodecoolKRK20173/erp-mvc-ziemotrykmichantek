""" Common functions for controllers
implement commonly used functions here
"""
from view import terminal_view
from model import data_manager

# def common_controller(create_function, update_function, delete_function, path):
#     options = ['Create',
#                'Read',
#                'Update',
#                'Delete']
#
#     terminal_view.print_menu(options,"Back to main menu")
#     choice = None
#     while choice != "0":
#         choice = terminal_view.get_choice(options)
#         if choice == "1":
#             create_function(data_manager.get_table_from_file(path), )
#         elif choice == "2":
#             update_function()
#         elif choice == "3":
#             delete_function()
#         else:
#             terminal_view.print_error_message("There is no such choice.")
