""" Common functions for models
implement commonly used functions here
"""
import random


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """


    # your code
    list_of_existing_keys = [record[0] for record in table]

    while True:
        generated = ''
        letters = 'abcdefghijklmnopqrstuvwxyz'
        generated+= random.choice(letters)
        genereated+='H'
        for i in range(2):
            generated+= str(random.randint(1,9))
        generated+= 'J'
        generated+= random.choice(letters)
        generated+= '#&'
        if generated not in list_of_existing_keys:
            break
    return generated

def common_add(table, record):
    record.insert(0, generate_random(table) )
    table.append(record)
    return table

def common_remove(table, id_):
    for line in table:
        if line[0]==id_:
            table.remove(line)
    return table

def common_update(table, id_, record):
    for i in range(len(table)):
        if table[i][0] == id_:
            table[i] = record
    return table
