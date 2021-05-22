from operator import itemgetter
import pandas as pd
import numpy as np

# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the requirements.


def display_inventory(inventory):
    """Display the contents of the inventory in a simple way."""
    for key, value in inventory.items():
        print(f"{key}: {value}")


def add_to_inventory(inventory, added_items):
    """Add to the inventory dictionary a list of items from added_items."""
    for key in added_items:
        if key in inventory.key():
            inventory[key] += 1
            continue
        inventory[key] = 1
    return inventory


def remove_from_inventory(inventory, removed_items):
    """Remove from the inventory dictionary a list of items from removed_items."""
    for key in removed_items:
        if key not in inventory.keys():
            continue
        inventory[key] -= 1
        if inventory[key] == 0:
            del inventory[key]
    return inventory


def print_table(inventory, order):
    """
    Display the contents of the inventory in an ordered, well-organized table with
    each column right-aligned.
    """
    order_list = ["count,desc", "count,asc"]
    sort_dict = inventory
    if order in order_list:
        if order == "count,asc":
            sort_dict = dict(sorted(inventory.items()))
        else:
            sort_dict = dict(sorted(test_inventory.items(), reverse=True))

    horiz_line = "-----------------"
    print(horiz_line)
    print("{:<10s} | {:>4s}".format(" item name", "count"))
    print(horiz_line)
    for key, value in sort_dict.items():
        print("{:>10s} | {:>4d}".format(key, value))
    print(horiz_line)


def import_inventory(inventory, filename):
    """Import new inventory items from a CSV file."""
    csv_inventory = pd.read_csv(filename, delimiter=",")
    df = list(csv_inventory)

    print(df)


def export_inventory(inventory, filename):
    """Export the inventory into a CSV file."""

    pass


test_inventory = {"pattern": 10, "pattern2": 50, "pattern1": 30}
"""removed_items = ['pattern3','pattern3']
display_inventory(remove_from_inventory(test_inventory, removed_items)) """

print_table(test_inventory, "")
print_table(test_inventory, "count,asc")
print_table(test_inventory, "count,desc")
import_inventory(test_inventory, "test_inventory.csv")
