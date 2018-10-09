# everything you'll need is imported:
from view import terminal_view
from controller import store_controller
from controller import hr_controller
from controller import inventory_controller
from controller import accounting_controller
from controller import sales_controller
from controller import crm_controller
from controller import common
from controller import data_analyser_controller
from data_analyser import data_analyser


def run():
    options = ["Store manager",
               "Human resources manager",
               "Inventory manager",
               "Accounting manager",
               "Sales manager",
               "Customer Relationship Management (CRM)",
               "Data anal yser"]

    choice = None
    while choice != "0":
        common.clear_function()
        terminal_view.print_primitive_logo()
        terminal_view.print_menu("Main menu: ", options, "Exit program")
        choice = terminal_view.get_choice()
        common.clear_function()
        if choice == "1":
            store_controller.run()
        elif choice == "2":
            hr_controller.run()
        elif choice == "3":
            inventory_controller.run()
        elif choice == "4":
            accounting_controller.run()
        elif choice == "5":
            sales_controller.run()
        elif choice == "6":
            crm_controller.run()
        elif choice == "7":
            data_analyser_controller.run()
        else:
            terminal_view.print_error_message("There is no such choice.")
