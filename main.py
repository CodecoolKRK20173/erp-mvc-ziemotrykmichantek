# Do not modify this file
# run this program (the ERP software) from the terminal from thd root directory of this project

from controller import root_controller


import sys
import view  # User Interface
# Store module
from model import store
# Human Resources module
from model import hr
# Tool manager module
from model import inventory
# Accounting module
from model import accounting
# Sales module
from model import sales
# Customer Relationship Management (CRM) module
from model import crm
# Data Analyser module
from data_analyser import data_analyser


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        store.start_module()
    elif option == "2":
        hr.start_module()
    elif option == "3":
        inventory.start_module()
    elif option == "4":
        accounting.start_module()
    elif option == "5":
        sales.start_module()
    elif option == "6":
        crm.start_module()
    elif option == "7":
        data_analyser.start_module()
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["Store manager",
               "Human resources manager",
               "Inventory manager",
               "Accounting manager",
               "Sales manager",
               "Customer Relationship Management (CRM)"]

    ui.print_menu("Main menu", options, "Exit program")

def main():
    root_controller.run()


if __name__ == '__main__':
    main()
