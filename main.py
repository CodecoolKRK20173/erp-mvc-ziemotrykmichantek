# Do not modify this file
# run this program (the ERP software) from the terminal from thd root directory of this project

from controller import root_controller


import sys
from music_player import play_soundtrack
from view import terminal_view  # User Interface
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

def main():
    root_controller.run()


if __name__ == '__main__':
    play_soundtrack.start()
    main()
